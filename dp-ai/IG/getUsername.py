import requests

# 사용자 액세스 토큰
access_token = 'EAAi2vEn6HSUBOwi7CiraeVKxTLYWyqrtk0nNitP8qg8FVA6abZAGKDyGKZCyWDfscaSP04LdGZCkpuRM1gZAP67l9jCjjMTuLZCOjSqv1vHNlcZC7bA3e3hnAJJTDWrS7ChL8lcKLbEIyZAjH2SX55aq7WXZCEwsx2pmgDhOw4IcRc6jwhWI000qCZCt4eM91vI2Pc3WjhcDMBVmsiMuSqkZBSHMdEFAZDZD'

# Graph API 요청 URL
url = f"https://graph.facebook.com/v12.0/me?fields=id,name,username&access_token={access_token}"

# API 요청 보내기
response = requests.get(url)

# 응답 데이터 처리
if response.status_code == 200:
    user_data = response.json()
    print(f"Name: {user_data.get('name')}")
    print(f"Username: {user_data.get('username')}")
else:
    print(f"Failed to retrieve data: {response.status_code}")
