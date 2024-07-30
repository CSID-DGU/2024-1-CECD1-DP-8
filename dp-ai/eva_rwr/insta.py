from instagrapi import Client
import getpass
from instagrapi.exceptions import LoginRequired
import logging

#request 사이에 delay 넣기
#cl.delay_range = [1, 3]

USERNAME = 'j_hcki_'
PASSWORD = getpass.getpass("pwd: ")
searchName = 'minsco_'

#간단한 로그인
'''
cl = Client()
cl.login(USERNAME, PASSWORD)
'''

logger = logging.getLogger()


"""
Attempts to login to Instagram using either the provided session information
or the provided username and password.
"""

cl = Client()
cl.login(USERNAME, PASSWORD)
cl.dump_settings("session.json")
session = cl.load_settings("session.json")

login_via_session = False
login_via_pw = False

if session:
    try:
        cl.set_settings(session)
        cl.login(USERNAME, PASSWORD)

        # check if session is valid
        try:
            cl.get_timeline_feed()
        except LoginRequired:
            logger.info("Session is invalid, need to login via username and password")

            old_session = cl.get_settings()

            # use the same device uuids across logins
            cl.set_settings({})
            cl.set_uuids(old_session["uuids"])

            cl.login(USERNAME, PASSWORD)
        login_via_session = True
    except Exception as e:
        logger.info("Couldn't login user using session information: %s" % e)

if not login_via_session:
    try:
        logger.info("Attempting to login via username and password. username: %s" % USERNAME)
        if cl.login(USERNAME, PASSWORD):
            login_via_pw = True
    except Exception as e:
        logger.info("Couldn't login user using username and password: %s" % e)

if not login_via_pw and not login_via_session:
    raise Exception("Couldn't login user with either password or session")


cl.delay_range = [1, 3]

#팔로워 수와 팔로잉 수
user = cl.user_info_by_username(searchName)
print("팔로워 수: ", user.follower_count, ", 팔로잉 수: ", user.following_count)
cl.delay_range = [1, 3]

#유저의 포스트 정보
user_id = user.pk
num = 2
medias = cl.user_medias(user_id, amount=num)  #amount: 가져올 미디어 개수
for media in medias :
    print("media id: ", media.id)
    print("like count: ", media.like_count)
    print("comment count: ", media.comment_count)
    print("caption text: ", media.caption_text)
    print("-------------------------------------------------")

    media_id = media.id

cl.delay_range = [1, 3]
print("마지막 글의 댓글들: ")
comments = cl.media_comments(media_id, amount=10)

#댓글 목록을 출력
for comment in comments:
    print("user: ", comment.user.username)
    print("comment: ", comment.text)
    print()
