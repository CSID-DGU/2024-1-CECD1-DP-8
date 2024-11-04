import requests
import statistics
import re

from config import GraphAPIConfig
from datetime import datetime
from fastapi import FastAPI, HTTPException
from utils import get_db_connection

app = FastAPI()


# 모든 인플루언서 유저 목록을 가져옴
def get_user_list_old():
    conn, cur = get_db_connection()
    if not conn or not cur:
        print("Failed to get user list due to database connection error.")
        return []
    cur.execute("SELECT nickname FROM influencer")
    user_list = [row['nickname'] for row in cur.fetchall()]  # 0번째 컬럼의 데이터
    cur.close()
    conn.close()
    return user_list


def get_user_list(cur):
    try:
        cur.execute("SELECT nickname FROM influencer")
        user_list = [row['nickname'] for row in cur.fetchall()]
        return user_list
    except Exception as e:
        print(f"<get user에서 오류 발생>")
        raise e


# influencer 테이블에 insert
@app.post("/influencer")
async def add_influencer():
    conn, cur = get_db_connection()
    if not conn or not cur:
        raise HTTPException(status_code=500, detail="Database connection failed")
    try:
        user_list = [
            ""
        ]
        for nickname in user_list:
            cur.execute("insert into influencer (nickname) values (%s)", (nickname,))
        conn.commit()
    except Exception as e:
        # 오류 발생 시 롤백
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error adding influencer: {e}")
    finally:
        cur.close()
        conn.close()

    return {"message": "Influencer added successfully"}


# 기존 코드
@app.get("/update")
def update():
    user_list = get_user_list()
    for username in user_list:
        api_url = (
            f"https://graph.facebook.com/v19.0/{GraphAPIConfig.user_id}"
            f"?fields=business_discovery.username({username})"
            f"{{biography,name,username,follows_count,profile_picture_url,"
            f"website,ig_id,followers_count,media_count,media.limit(30)"
            f"{{caption,comments_count,id,children{{media_url,media_type}},"
            f"like_count,media_product_type,media_type,media_url,owner,permalink,timestamp,username}}}}"
            f"&access_token={GraphAPIConfig.access_token}"
        )

        response_json = requests.get(api_url).json()

        print(response_json)

        # media 테이블 업데이트
        conn, cur = get_db_connection()
        if not conn or not cur:
            raise HTTPException(status_code=500, detail="Database connection failed")

        cur.execute("SELECT * FROM influencer WHERE nickname=%s", (username,))
        user_id = cur.fetchall()[0][0]

        media_list = response_json["business_discovery"]["media"]["data"]

        for media in media_list:
            try:
                data = {
                    "collected_date": datetime.today().strftime("%Y-%m-%d"),
                    "comment_cnt": media["comments_count"],
                    "creation_date": media["timestamp"][:10],
                    "like_cnt": media["like_count"],
                    "user_id": user_id,
                    "caption": media["caption"].replace("\n", " "),
                    "insta_media_id": media["id"],
                }

                print(data)

                insert_query = """
                    INSERT INTO media (collected_date, comment_cnt, creation_date, like_cnt, user_id, caption, insta_media_id)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """

                cur.execute(insert_query, (
                    data["collected_date"],
                    data["comment_cnt"],
                    data["creation_date"],
                    data["like_cnt"],
                    data["user_id"],
                    data["caption"],
                    data["insta_media_id"]
                ))

                conn.commit()
            except:
                continue

        # meta 테이블 업데이트
        collected_date = datetime.today().strftime("%Y-%m-%d")

        cur.execute("SELECT * FROM media WHERE user_id=%s AND collected_date=%s", (user_id, collected_date,))

        rows = cur.fetchall()

        comment_cnt_list = []
        like_cnt_list = []

        for row in rows:
            comment_cnt_list.append(row[1])
            like_cnt_list.append(row[3])

        # print(comment_cnt_list)
        # print(like_cnt_list)

        sql = """
            INSERT INTO meta (collected_date, follower_cnt, comment_avg, like_avg, user_id)
            VALUES (%s, %s, %s, %s, %s);
        """

        data = {
            "collected_date": collected_date,
            "follower_cnt": response_json["business_discovery"]["followers_count"],
            "comment_avg": statistics.mean(comment_cnt_list),
            "like_avg": statistics.mean(like_cnt_list),
            "user_id": user_id
        }

        cur.execute(sql, (
            data["collected_date"],
            data["follower_cnt"],
            data["comment_avg"],
            data["like_avg"],
            data["user_id"]
        ))

        # 변경사항 커밋
        conn.commit()

        cur.close()
        conn.close()


# influencer 테이블 업데이트
def update_influencer_account(cur, account_data, influencer_pk):
    try:
        query = '''
                    update influencer
                    set graph_id=%s,nickname=%s,name=%s,biography=%s,profile_picture_url=%s,website=%s
                    where influencer_id=%s
                    '''

        # account_data json에서 key가 존재하지 않을 경우 빈 문자열 사용
        graph_id = account_data.get("id")
        nickname = account_data.get("username")
        name = account_data.get("name", "")
        biography = account_data.get("biography", "")
        profile_picture_url = account_data.get("profile_picture_url", "")
        website = account_data.get("website", "")

        cur.execute(query, (
            graph_id,
            nickname,
            name,
            biography,
            profile_picture_url,
            website,
            influencer_pk
        ))

    except Exception as e:
        print(f"<update_influencer_account에서 오류 발생>")
        raise e


# media에 있는 해시태그를 hashtag 및 media_hashag에 저장
def insert_media_hashtags(cur, media_pk: int, caption):
    try:
        # 해시태그 리스트 추출
        hashtag_list = re.findall(r"#(\w+)", caption)
        #print(f"hashtag list: {hashtag_list}")
        for hashtag in hashtag_list:
            cur.execute("SELECT hash_tag_id FROM hash_tag WHERE name = %s", (hashtag,))
            hashtag_result = cur.fetchone()

            if hashtag_result is None:
                # 저장되어있지 않은 해시태그인 경우, hashtag 테이블에 insert
                cur.execute("INSERT INTO hash_tag (name) VALUES (%s) RETURNING hash_tag_id", (hashtag,))
                hashtag_id = cur.fetchone()["hash_tag_id"]
            else:
                hashtag_id = hashtag_result["hash_tag_id"]

            # media_id와 hash_tag_id를 media_hashtag 테이블에 insert하기
            cur.execute("INSERT INTO media_hash_tag (media_id, hash_tag_id) VALUES (%s, %s)", (media_pk, hashtag_id))
        return {"message": "Hashtags processed successfully"}

    except Exception as e:
        print(f"<insert_media_hashtags에서 오류 발생>")
        print(f"media_id: {media_pk}")
        raise e


# image 테이블에 insert하는 함수
def insert_image(cur, media_id: int, image_url: str, media_type, id):
    try:
        cur.execute("insert into image (media_id, image_url, object_type, graph_id) values (%s, %s, %s, %s)", (
            media_id, image_url, media_type, id))
        return {"message": f"image 데이터 insert 성공"}
    except Exception as e:
        print(f"<image insert에서 오류 발생>")
        raise e


def get_db_media_id_from_graph_media_id(graph_media_id, cur):
    try:
        cur.execute("select media_id from media where graph_media_id = %s", (graph_media_id,))
        result = cur.fetchone()
        if result:
            return result["media_id"]
        else:
            raise Exception("graph_media_id로부터 media id를 찾을 수 없음")
    except Exception as e:
        print("<get_db_media_id_from_graph_media_id에서 오류 발생")
        raise e


# 인플루언서 계정 데이터 가져오기
def get_account_data(username):
    try:
        api_url = (
            f"https://graph.facebook.com/v19.0/{GraphAPIConfig.user_id}"
            f"?fields=business_discovery.username({username})"
            f"{{biography,id,ig_id,followers_count,follows_count,media_count,"
            f"name,profile_picture_url,username,website}}"
            f"&access_token={GraphAPIConfig.access_token}"
        )
        '''
        요청 응답 예시
        {
          "business_discovery": {
            "biography": "💜콜라보 마켓 진행중💜",
            "id": "....",
            "ig_id": ....,
            "followers_count": 113266,
            "follows_count": 567,
            "media_count": 1621,
            "name": "설정한 이름",
            "profile_picture_url": "https://...",
            "username": "username._.hi",
            "website": "https://...."
          },
          "id": "나의 instagram id"
        }
        '''

        account_data = requests.get(api_url).json()
        account_data = account_data["business_discovery"]
        #print(f"account_data: {account_data}")
        return account_data
    except Exception as e:
        print("<get_account_data에서 오류 발생>")
        raise e


# 일정 개수의 최신 미디어 가져오기
def get_recent_media(username, media_num, after_cursor):
    try:
        if after_cursor == "":
            print(f"after cursor 없음!")
            api_url = (
                f"https://graph.facebook.com/v19.0/{GraphAPIConfig.user_id}"
                f"?fields=business_discovery.username({username})"
                f"{{media.limit({media_num})"
                f"{{id,comments_count,like_count,media_product_type,media_type,media_url,"
                f"owner,permalink,thumbnail_url,timestamp,username,children{{media_url,media_type}},caption}}}}"
                f"&access_token={GraphAPIConfig.access_token}"
            )
        else:
            print("after cursor 있음!")
            api_url = (
                f"https://graph.facebook.com/v19.0/{GraphAPIConfig.user_id}"
                f"?fields=business_discovery.username({username})"
                f"{{media.limit({media_num}).after({after_cursor})"
                f"{{id,comments_count,like_count,media_product_type,media_type,media_url,"
                f"owner,permalink,thumbnail_url,timestamp,username,children{{media_url,media_type}},caption}}}}"
                f"&access_token={GraphAPIConfig.access_token}"
            )

        media_list = requests.get(api_url).json()
        media_list = media_list["business_discovery"]["media"]
        return media_list
    except Exception as e:
        print("<get_recent_media에서 오류 발생>")
        raise e


def get_influencer_pk_from_username(cur, username):
    try:
        cur.execute("select influencer_id from influencer where nickname = %s", (username,))
        result = cur.fetchone()
        if result:
            return result["influencer_id"]
        else:
            raise Exception("username으로부터 influencer_id를 찾을 수 없음")
    except Exception as e:
        print("<get_influencer_id_from_username에서 오류 발생")
        raise e


# meta 테이블에 insert하는 함수. 평균 등등 계산
# 평균 구하는 기준... 최근 100개 or 모든 게시글?
def insert_meta(cur, influencer_id, account_data):
    try:
        collected_datetime = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        print(f"collected: {collected_datetime}")

        cur.execute("SELECT comments_cnt,like_cnt FROM media WHERE influencer_id=%s", (influencer_id,))
        rows = cur.fetchall()

        comment_cnt_list = []
        like_cnt_list = []

        for row in rows:
            if row['comments_cnt'] is not None:
                comment_cnt_list.append(row['comments_cnt'])
            if row['like_cnt'] is not None:
                like_cnt_list.append(row['like_cnt'])

        query = """
                    INSERT INTO meta (influencer_id,like_avg,comments_avg,follower_cnt,follows_cnt,created_at)
                    VALUES (%s, %s, %s, %s, %s, %s);
                """

        data = {
            "influencer_id": influencer_id,
            "like_avg": statistics.mean(like_cnt_list),
            "comments_avg": statistics.mean(comment_cnt_list),
            "follower_cnt": account_data["followers_count"],
            "follows_cnt": account_data["follows_count"],
            "created_at": collected_datetime
        }

        cur.execute(query, (
            data["influencer_id"],
            data["like_avg"],
            data["comments_avg"],
            data["follower_cnt"],
            data["follows_cnt"],
            data["created_at"]
        ))
    except Exception as e:
        print("<insert_meta에서 오류 발생>")
        raise e


# media insert
def insert_media(cur, media, influencer_id, media_type, username):
    try:
        collected_datetime = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

        # media["timestamp"] 형식 변환
        timestamp_str = media["timestamp"]  # "2024-04-26T02:41:46+0000"
        timestamp_dt = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S%z")
        timestamp = timestamp_dt.strftime("%Y-%m-%d %H:%M:%S")

        caption = media.get("caption", "")
        # 광고글 판단
        keywords = ["#광고", "#협찬", "#제품제공", "#제품협찬", "#서포터즈", "유료광고", "대가성광고"]
        is_ad = any(keyword in caption for keyword in keywords)

        # thumbnail_url을 특정 형식으로 변경
        thumbnail_url = media["permalink"]
        thumbnail_url = thumbnail_url + "media/?size=l"
        thumbnail_url = thumbnail_url.replace("reel", "p")
        thumbnail_url = thumbnail_url.replace(f"{username}/", "")


        # VIDEO가 아닌 경우, "thumbnail_url"이 존재하지 않으며 "media_url"이 그 역할을 함
        # VIDEO인 경우, "media_url"은 동영상 url이며, media json에 존재하지 않을 수도 있음
        # VIDEO인 경우, "thumbnail_url" 존재. 동영상의 썸네일 사진 링크
        if media_type == "VIDEO": # REELS, 일부 옛날 게시글의 경우 FEED도 있음
            #thumbnail_url = media.get("thumbnail_url", "")
            video_url = media.get("media_url", "")

        else:  # IMAGE, CAROUSEL_ALBUM
            # IMAGE 사진 id를 알 수 없으므로 thumbnail_url에만 사진 링크를 저장하고 image에는 저장하지 않음
            #thumbnail_url = media["media_url"]
            video_url = ""
            '''
            {
              "comments_count": 1,
              "media_url": "https://scontent....",
              "timestamp": "2019-12-05T13:05:24+0000",
              "id": "1785000374573....",
              "like_count": 157,
              "media_product_type": "FEED",
              "media_type": "IMAGE"
            }
            '''

        # 좋아요 숨기기 할 경우
        like_cnt = media.get("like_count", -1)

        query = '''
            INSERT INTO media (influencer_id, graph_media_id, comments_cnt, like_cnt, media_product_type,
                               media_type, perma_link, is_ad, caption, posted_at, created_at, updated_at,
                               thumbnail_url, video_url)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)

        '''

        cur.execute(query, (
            influencer_id,
            media["id"],
            media["comments_count"],
            like_cnt,
            media["media_product_type"],
            media["media_type"],
            media["permalink"],
            is_ad,
            caption,
            timestamp,
            collected_datetime, collected_datetime,
            thumbnail_url,
            video_url
        ))

    except Exception as e:
        print(f"<insert_media에서 오류 발생>")
        print(f"media: {media}")
        print(f"influencer_pk: {influencer_id}")
        raise e


def insert_all_user_data(username: str):
    conn, cur = get_db_connection()
    if not conn or not cur:
        raise HTTPException(status_code=500, detail="Database connection failed")

    try:
        # influencer의 계정 데이터 가져오기
        account_data = get_account_data(username)

        # influencer pk 얻기
        influencer_pk = get_influencer_pk_from_username(cur, username)

        # influencer 계정 데이터 update
        update_influencer_account(cur, account_data, influencer_pk)

        # 인플루언서의 media 데이터 가져오기
        # 최근 100개의 게시물
        # 100개를 한번에 가져올 수 없어서 두번에 나누어 가져옴. after cursor 사용
        media_num = 50
        after_cursor = ""
        for i in range(2):
            media_list = get_recent_media(username, media_num, after_cursor)
            '''
            {
                "data": [media list...],
                "paging": {
                    "cursors": {
                      "after": "kyM..."
                    }
                  }
            }
            '''
            paging_data = media_list.get('paging')
            if paging_data:
                cursor_data = paging_data.get('cursors')
                if 'after' in cursor_data:
                    after_cursor = cursor_data["after"]
                    print(f"after_cursor: {after_cursor}")
            media_list = media_list["data"]

            # 미디어와 이미지 insert
            for media in media_list:
                # 미디어가 여러개 - media_type: "CAROUSEL_ALBUM", children 존재함
                # 미디어가 하나의 사진 - media_type: "IMAGE", children 존재하지 않음
                # 미디어가 하나의 비디오 - media_type: "VIDEO", children 존재하지 않음
                # media_product_type으로 구분하지 않는 이유: 하나의 동영상일 경우에는 FEED가 아니라 REELS로 올라가지만
                #                                        일부 옛날 게시글은 동영상 하나도 FEED일 수 있음.
                media_type = media["media_type"]

                if media_type == "VIDEO":
                    # 미디어 insert
                    insert_media(cur, media, influencer_pk, media_type, username)

                elif media_type == "IMAGE":
                    # IMAGE 사진 id를 알 수 없으므로 thumbnail_url에만 사진 링크를 저장하고 image에는 저장하지 않음
                    ''' 
                    {
                      "comments_count": 28,
                      "caption": "6월10일 네이버 인플고시 합격했어요🫶🏻 고생하긴 했습니다..😂",
                      "media_url": "https://scontent....",
                      "like_count": 223,
                      "media_product_type": "FEED",
                      "media_type": "IMAGE",
                      "id": "17927721...."
                    }
                    '''
                    insert_media(cur, media, influencer_pk, media_type, username)

                else:
                    # media["media_type"] == "CAROUSEL_ALBUM"
                    # 미디어 insert
                    insert_media(cur, media, influencer_pk, media_type, username)

                    # 이미지 insert
                    media_id = get_db_media_id_from_graph_media_id(media["id"], cur)
                    # print(f"media table의 pk: {media_id}")

                    if media_type == "CAROUSEL_ALBUM":
                        image_list = media["children"]["data"]
                        for image in image_list:
                            # 아래와 같이 오류로 인해 media_url이 없는 경우는 insert에서 제외
                            '''
                            "children": {
                                "data": [
                                  {
                                    "media_type": "VIDEO",
                                    "id": "18127329......."
                                  },
                            '''
                            if image.get("media_url") is not None:
                                insert_image(cur, media_id, image["media_url"], image["media_type"], image["id"])

                media_id = get_db_media_id_from_graph_media_id(media["id"], cur)
                # hashtag, media_hashtag insert
                # caption이 존재하지 않는 경우에는 실행X
                if "caption" in media:
                    insert_media_hashtags(cur, media_id, media["caption"])

            # 전체 게시글이 50개 이하인 경우
            if paging_data is None:
                print("전체 게시글이 50개 이하입니다.")
                break


        # meta 테이블에 insert
        insert_meta(cur, influencer_pk, account_data)

        # 모든 작업이 성공적으로 완료되면 커밋
        conn.commit()
        return {"status": "success"}
    except Exception as e:
        conn.rollback()
        print("<insert_all_user_data>에서 오류 발생")
        raise e
        #return {"status": "failed", "reason": str(e)}
    finally:
        cur.close()
        conn.close()


# 새로운 인플루언서 등록 시, 초기 데이터 수집 및 저장(influencer, media, hashtag 테이블)
@app.post("/influencers/data")
async def update_and_insert_influencers_data():
    try:
        user_list = [
            ""
        ]

        for user in user_list:
            print(f"{user}의 초기 정보 수집 시작......")
            insert_all_user_data(user)
            print(f"{user} 정보 수집 완료")
            print("===============================================")

    except Exception as e:
        print(f"Error : {e}")
        return {"status": "failed", "reason": str(e)}

    else:
        print("data 수집 성공!")


# media의 graph_id로 검색해 이미 수집된 미디어인지 확인
def check_media_pk_from_graph_media_id(cur, graph_media_id):
    try:
        query = "SELECT media_id FROM media WHERE graph_media_id = %s"
        cur.execute(query, (graph_media_id,))

        # 미디어가 존재하는지 확인 (존재하지 않으면 None 반환)
        media_row = cur.fetchone()

        if media_row:
            return media_row['media_id']
        else:
            return None
    except Exception as e:
        print(f"<is_collected_media에서 오류 발생>")
        raise e

# 미디어 업데이트
def update_media(cur, media):
    try:
        updated_datetime = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

        # VIDEO가 아닌 경우, "thumbnail_url"이 존재하지 않으며 "media_url"이 그 역할을 함
        # VIDEO인 경우, "media_url"은 동영상 url이며, media json에 존재하지 않을 수도 있음
        # VIDEO인 경우, "thumbnail_url" 존재. 동영상의 썸네일 사진 링크
        if media["media_type"] == "VIDEO":  # REELS, 일부 옛날 게시글의 경우 FEED도 있음
            #thumbnail_url = media.get("thumbnail_url", "")
            video_url = media.get("media_url", "")

        else:  # IMAGE, CAROUSEL_ALBUM
            # IMAGE 사진 id를 알 수 없으므로 thumbnail_url에만 사진 링크를 저장하고 image에는 저장하지 않음
            #thumbnail_url = media["media_url"]
            video_url = ""
            '''
            {
              "comments_count": 1,
              "media_url": "https://scontent...",
              "timestamp": "2019-12-05T13:05:24+0000",
              "id": "178500037....",
              "like_count": 157,
              "media_product_type": "FEED",
              "media_type": "IMAGE"
            }
            '''

        # 좋아요 숨기기 할 경우
        like_cnt = media.get("like_count", -1)

        query = '''
                    update media set
                    comments_cnt=%s, like_cnt=%s, updated_at=%s, video_url=%s
                    where graph_media_id=%s

                '''

        cur.execute(query, (
            media["comments_count"],
            like_cnt,
            updated_datetime,
            video_url,
            media["id"]
        ))
    except Exception as e:
        print(f"<update_media에서 오류 발생>")
        print(f"media: {media}")
        raise e

# 미디어, 이미지, 해시태그 insert
def insert_media_image_hashtag(cur, media, influencer_pk, username):
    try:
        # 미디어가 여러개 - media_type: "CAROUSEL_ALBUM", children 존재함
        # 미디어가 하나의 사진 - media_type: "IMAGE", children 존재하지 않음
        # 미디어가 하나의 비디오 - media_type: "VIDEO", children 존재하지 않음
        # media_product_type으로 구분하지 않는 이유: 하나의 동영상일 경우에는 FEED가 아니라 REELS로 올라가지만
        #                                        일부 옛날 게시글은 동영상 하나도 FEED일 수 있음.
        media_type = media["media_type"]

        if media_type == "VIDEO":
            # 미디어 insert
            insert_media(cur, media, influencer_pk, media_type, username)

        elif media_type == "IMAGE":
            # IMAGE 사진 id를 알 수 없으므로 thumbnail_url에만 사진 링크를 저장하고 image에는 저장하지 않음
            ''' 
            {
              "comments_count": 28,
              "caption": "6월10일 네이버 합격했어요😂",
              "media_url": "https://scontent....",
              "like_count": 223,
              "media_product_type": "FEED",
              "media_type": "IMAGE",
              "id": "179277215......."
            }
            '''
            insert_media(cur, media, influencer_pk, media_type, username)

        else:
            # media["media_type"] == "CAROUSEL_ALBUM"
            # 미디어 insert
            insert_media(cur, media, influencer_pk, media_type, username)

            # 이미지 insert
            media_id = get_db_media_id_from_graph_media_id(media["id"], cur)
            # print(f"media table의 pk: {media_id}")

            if media_type == "CAROUSEL_ALBUM":
                image_list = media["children"]["data"]
                for image in image_list:
                    # 아래와 같이 오류로 인해 media_url이 없는 경우는 insert에서 제외
                    '''
                    "children": {
                        "data": [
                          {
                            "media_type": "VIDEO",
                            "id": "1812732..........."
                          },
                    '''
                    if image.get("media_url") is not None:
                        insert_image(cur, media_id, image["media_url"], image["media_type"], image["id"])

        media_id = get_db_media_id_from_graph_media_id(media["id"], cur)
        # hashtag, media_hashtag insert
        # caption이 존재하지 않는 경우에는 실행X
        if "caption" in media:
            insert_media_hashtags(cur, media_id, media["caption"])
    except Exception as e:
        print(f"<insert_media_image_hashtag에서 오류 발생>")
        raise e


def update_user(username):
    conn, cur = get_db_connection()
    if not conn or not cur:
        raise HTTPException(status_code=500, detail="Database connection failed")

    try:
        # === influencer table 업데이트 ===
        # influencer의 계정 데이터 가져오기
        account_data = get_account_data(username)

        # influencer pk 얻기
        influencer_pk = get_influencer_pk_from_username(cur, username)

        # influencer 계정 데이터 update
        update_influencer_account(cur, account_data, influencer_pk)

        # === 최근 30개의 미디어에 대해, 새로운 미디어는 insert하고 기존 미디어는 update ===
        media_num = 30
        media_list = get_recent_media(username, media_num, "")
        '''
        {
            "data": [media list...],
            "paging": {
                "cursors": {
                  "after": "kyM..."
                }
            }
        }
        '''
        media_list = media_list["data"]

        for media in media_list:
            media_graph_id = media["id"]
            # graph_id로 검색해 이미 수집된 미디어인지 확인
            # 이미 수집된 미디어의 경우 update 수행
            media_pk = check_media_pk_from_graph_media_id(cur, media_graph_id)
            if media_pk:
                update_media(cur, media)

            else:
                # media insert
                insert_media_image_hashtag(cur, media, influencer_pk, username)

        # === meta 테이블에 insert ===
        insert_meta(cur, influencer_pk, account_data)

        # 모든 작업이 성공적으로 완료되면 커밋
        conn.commit()
        return {"status": "success"}
    except Exception as e:
        conn.rollback()
        print(f"E: {e}")
        print("<update_user>에서 오류 발생")
        raise e
        #return {"status": "failed", "reason": str(e)}
    finally:
        cur.close()
        conn.close()

# 인플루언서 정보 업데이트
# influncer 업데이트, 최신 30개 미디어에 대해 media 업데이트(일단 이미지 제외..) 혹은 insert, meta insert
@app.put("/influencers/data")
async def update():
    try:
        # 모든 인플루언서 nickname 가져오기
        user_list = get_user_list_old()

        #user_list = [
        #
        #]

        completed_user_list = []
        print(f"user_list: {user_list}")
        for username in user_list:
            print(f"{username}의 정보 업데이트 시작......")
            update_user(username)
            print(f"{username} 정보 업데이트 완료!")
            print("===============================================")
            completed_user_list.append(username)

    except Exception as e:
        print(f"Error : {e}")
        return {"status": "failed", "reason": str(e)}
    else:
        print("data 업데이트 성공!")
        return {"status": "success"}
    finally:
        print(f"정보 수집 완료 유저: {completed_user_list}")
        uncompleted_users = list(set(user_list) - set(completed_user_list))
        print(f"정보 수집 해야하는 유저: {uncompleted_users}")


@app.get("/")
async def root():
    conn, cur = get_db_connection()
    if not conn or not cur:
        raise HTTPException(status_code=500, detail="Database connection failed")
    user_list = get_user_list(cur)
    return {"users": user_list}


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}