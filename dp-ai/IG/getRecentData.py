import requests
import json
import schedule
import time
from datetime import datetime, timedelta

def getRecentData(username):
    accessToken = ""
    userID = ""
    afterCursor = ""
    call_count = 0
    media_count = 0

    #정보 갱신, 추가
    if username:
        while True:
            if call_count >= 3:  # 3번까지만 호출하도록 제한. 최신 게시글 52개의 정보 갱신, 추가
                break

            if afterCursor != "":
                api_url = ("https://graph.facebook.com/v19.0/"+userID+
                           "?fields=business_discovery.username("+username+"){"
                                "name,username,ig_id,followers_count,media_count,media.after("+afterCursor+"){"
                                "caption,comments_count,id,children{media_url,media_type},like_count,media_product_type,media_type,media_url,owner,permalink,timestamp,username}"
                           "}&access_token=" + accessToken)
            else:
                api_url = "https://graph.facebook.com/v19.0/"+userID+"?fields=business_discovery.username("+username+"){biography,name,username,follows_count,profile_picture_url,website,ig_id,followers_count,media_count,media.limit(2){caption,comments_count,id,children{media_url,media_type},like_count,media_product_type,media_type,media_url,owner,permalink,timestamp,username}}&access_token="+accessToken
                print(api_url)
            response = requests.get(api_url)

            if response.status_code == 200:
                print("HTTP response 200")
                user_data = response.json()

                #media 개수(모든 게시글 정보를 가져오는지 확인하기 위해)
                media_count += len(user_data['business_discovery']['media']['data'])
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

                # 정보 갱신 & 새로운 게시글 추가


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
    print(username, ' 정보 갱신 종료\n')

    #최근 한달간의 게시글 데이터 가져오기

    like_count = 0      #한달간의 좋아요 총 개수
    average_like = 0    #좋아요 평균
    media_count = 0     #한달간 올린 미디어 개수
    
    follwer_change = 0  #팔로워 수 변동
    #그 외의 지표들

    #현재 날짜
    current_date = datetime.now().date()
    #한 달 전의 날짜
    one_month_ago = current_date - timedelta(days=30)
    since_date = one_month_ago.strftime("%Y-%m-%d")
    until_date = current_date.strftime("%Y-%m-%d")
    if username:
        #db에서 정보 가져옴
        pass

    print('실행 종료')

username = ["bop.pt", "lav_ender_11_2"]
for name in username:
    userdata = getRecentData(name)

'''
# 매일 정오에 job 함수를 실행하도록 예약
for name in username:
    schedule.every().day.at("12:00").do(getRecentData, name)

while True:
    # 예약된 작업을 실행
    schedule.run_pending()
    time.sleep(60)
'''