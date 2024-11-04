# 실행 방법

## 1. Setup config.py
fast_api_server 폴더 아래에 config.py 파일을 만듭니다.
>config.py

    class PostgresConfig:
    dbname = "..."
    user = "..."
    password = "your_password"
    host = "주소"
    port = "5432"


    class GraphAPIConfig:
        user_id = "178.............."
        access_token = "............"
테스트용으로 로컬 데이터베이스를 사용할 시, host 주소는 127.0.0.1 
## 2. main.py 실행
    uvicorn main:app --reload

## 3. Postman으로 request 전송
> 신규 인플루언서 데이터 수집

    [POST]http://127.0.0.1:8000/influencers/data

> 데이터 업데이트

    [PUT]http://127.0.0.1:8000/influencers/data