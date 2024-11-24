import requests
from config import GraphAPIConfig

def check_business_accounts(usernames, access_token):
    business_accounts = []
    non_business_accounts = []
    for username in usernames:
        url = f"https://graph.facebook.com/v12.0/{GraphAPIConfig.user_id}"
        params = {
            'fields': f'business_discovery.username({username}){{biography,name,username,follows_count,profile_picture_url,website,ig_id,followers_count,media_count,media.limit(1){{caption,comments_count,id,children{{media_url,media_type}},like_count,media_product_type,media_type,media_url,owner,permalink,timestamp,username}}}}',
            'access_token': access_token
        }

        response = requests.get(url, params=params)
        if response.status_code == 200:
            business_accounts.append(username)
        else:
            # 오류 메시지를 통해 비즈니스 계정 여부 확인
            error_data = response.json()
            error_message = error_data.get("error", {}).get("error_user_title", "")
            if "사용자를 찾을 수 없습니다" in error_message:
                non_business_accounts.append(username)
            else:
                print(f"다른 오류 발생 - {username}: {error_message}")

    return business_accounts, non_business_accounts


usernames = [

]
access_token = GraphAPIConfig.access_token
business_accounts, non_business_accounts = check_business_accounts(usernames, access_token)

print("비즈니스 계정:", business_accounts)
print("비즈니스 계정이 아닌 계정:", non_business_accounts)
