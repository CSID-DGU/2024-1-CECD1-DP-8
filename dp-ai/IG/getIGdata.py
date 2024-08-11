import requests
import json
import schedule
import time
'''
def deleteTbAccount(username):
    pass


def insertTbAccount(business_discovery_data):
    pass


def deleteTbAccountSnapshot(param):
    pass


def insertTbAccountSnapshot(business_discovery_data):
    pass


def deleteUserFix(business_discovery_data):
    pass


def insertUserFix(business_discovery_data):
    pass


def deleteUsersInfo(business_discovery_data):
    pass


def insertUsersInfo(business_discovery_data):
    pass


def deleteComment(ig_id):
    pass


def insertComment(business_discovery_data):
    pass


def deleteTbMedia(mediaList):
    pass


def insertTbMedia(mediaList, followers_cnt):
    pass


def deleteTbMediaAlbum(mediaList):
    pass


def InsertTbMediaAlbum(mediaList):
    pass

def deleteTbMediaSnapShot(mediaList):
    pass


def InsertTbMediaSnapShot(mediaList):
    pass


def deleteTbMediaHashTag(mediaList):
    pass


def insertTbMediaHashTag(mediaList):
    pass


def deleteHashtags(mediaList):
    pass


def insertHashtags(mediaList):
    pass


def deleteFeed(mediaList, ig_id):
    pass


def insertFeed(mediaList, param):
    pass


def insertMediaFix(mediaList, ig_id):
    pass


def deleteMediaFix(mediaList, ig_id):
    pass


def deleteMediaInfo(mediaList, ig_id):
    pass


def insertMediaInfo(mediaList, ig_id):
    pass

'''
def callInstagramAPI(username):
    accessToken = ""
    userID = ""
    afterCursor = ""
    call_count = 0
    media_count = 0

    if username:
        while True:
            if call_count >= 3:
                print("10초 딜레이...")
                time.sleep(10)
                print("10초가 경과되었습니다.")
                call_count = 0
                continue

            if afterCursor != "":
                api_url = ("https://graph.facebook.com/v19.0/"+userID+
                           "?fields=business_discovery.username("+username+"){"
                                "name,username,ig_id,followers_count,media_count,media.after("+afterCursor+"){"
                                "caption,comments_count,id,children{media_url,media_type},like_count,media_product_type,media_type,media_url,owner,permalink,timestamp,username}"
                           "}&access_token=" + accessToken)
            else:
                api_url = "https://graph.facebook.com/v19.0/"+userID+"?fields=business_discovery.username("+username+"){biography,name,username,follows_count,profile_picture_url,website,ig_id,followers_count,media_count,media.limit(2){caption,comments_count,id,children{media_url,media_type},like_count,media_product_type,media_type,media_url,owner,permalink,timestamp,username}}&access_token="+accessToken
                #print(api_url)
            response = requests.get(api_url)

            if response.status_code == 200:
                print("HTTP response 200")
                user_data = response.json()

                #media 개수(모든 게시글 정보를 가져오는지 확인하기 위해)
                media_count += len(user_data['business_discovery']['media']['data'])
                print('################################', media_count)
                #json 데이터를 보기 좋게 출력
                print(json.dumps(user_data, indent=4, ensure_ascii=False))

                business_discovery_data = user_data.get('business_discovery', {})
                media = business_discovery_data.get('media')
                pagingData = media.get('paging')
                cursorData = pagingData.get('cursors')
                print()
                mediaList = media.get('data') #게시글 리스트
                followers_cnt = business_discovery_data.get('followers_count')
                ig_id = business_discovery_data.get('ig_id')

                #데이터베이스 작업
                if afterCursor == "":
                    '''
                    deleteTbAccount(username)
                    insertTbAccount(business_discovery_data)
                    deleteTbAccountSnapshot(user_data.get('id'))
                    insertTbAccountSnapshot(business_discovery_data)
                    deleteUserFix(business_discovery_data)
                    insertUserFix(business_discovery_data)
                    deleteUsersInfo(business_discovery_data)
                    insertUsersInfo(business_discovery_data)
                    deleteComment(ig_id)
                    insertComment(business_discovery_data)

                deleteTbMedia(mediaList)
                insertTbMedia(mediaList, followers_cnt)

                deleteTbMediaAlbum(mediaList)
                InsertTbMediaAlbum(mediaList)

                deleteTbMediaSnapShot(mediaList)
                InsertTbMediaSnapShot(mediaList)

                deleteTbMediaHashTag(mediaList)
                insertTbMediaHashTag(mediaList)

                deleteHashtags(mediaList)
                insertHashtags(mediaList)

                deleteFeed(mediaList, ig_id)
                insertFeed(mediaList, business_discovery_data.get('id'))

                deleteMediaFix(mediaList, ig_id)
                insertMediaFix(mediaList, ig_id)

                deleteMediaInfo(mediaList, ig_id)
                insertMediaInfo(mediaList, ig_id)
                '''

                if 'after' in cursorData:
                    afterCursor = cursorData['after']
                    call_count += 1  # 호출 횟수 증가
                else:
                    break
            elif response.status_code == 403:
                msg = '403'
                print('실행 결과', msg)
                return msg
            else:
                msg = response.status_code
                print('실행 결과', msg)
                return msg

    print('media count: ', media_count)
    print(username, ' 실행 종료')


username = ["bop.pt", "for_everyoung10"]
for name in username:
    userdata = callInstagramAPI(name)