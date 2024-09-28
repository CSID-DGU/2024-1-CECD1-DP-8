import openai
import psycopg2
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import random  # 테스트용으로 가중치 대신 사용

# PostgreSQL 연결 설정 - 환경변수에서 값 가져오기
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

app = FastAPI()

# OpenAI GPT API 키 설정 - 환경변수에서 값 가져오기
openai.api_key = os.getenv("OPENAI_API_KEY")

# 필터링 기준을 담을 데이터 모델 정의
class FilterRequest(BaseModel):
    category: str
    min_followers: int
    max_followers: int
    gender: str
    keywords: list[str]

# PostgreSQL 연결 함수 (DB 연결 성공 여부 출력)
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        print("DB 연결 성공")
        return conn
    except psycopg2.DatabaseError as e:
        print(f"DB 연결 실패: {e}")
        raise HTTPException(status_code=500, detail="DB 연결 실패")

# 1차 필터링 함수 (연관 해시태그 기반 필터링된 인플루언서)
def get_influencers_by_hashtags(filters: FilterRequest, conn):
    cursor = conn.cursor()

    # 필터링된 해시태그를 바탕으로 인플루언서 조회
    query = """
    SELECT i.name, i.profile_picture_url, i.biography 
    FROM influencer i
    JOIN meta m ON i.influencer_id = m.influencer_id
    JOIN media me ON me.influencer_id = i.influencer_id
    WHERE i.category = %s
    AND m.follower_cnt BETWEEN %s AND %s
    AND i.gender = %s
    AND me.caption LIKE ANY(%s);
    """
    
    # '%'를 키워드 앞뒤에 추가하여 부분 일치 검색
    hashtags_like = [f"%{keyword}%" for keyword in filters.keywords]
    
    cursor.execute(query, (filters.category, filters.min_followers, filters.max_followers, filters.gender, hashtags_like))
    influencers = cursor.fetchall()
    
    return influencers

# 1차 필터링 (정량적 데이터 + 해시태그 기반)
@app.post("/recommend")
async def recommend_influencers(filters: FilterRequest):
    try:
        conn = get_db_connection()

        # 필터링된 인플루언서 목록을 가져옴
        influencers = get_influencers_by_hashtags(filters, conn)

        # 필터링된 인플루언서 리스트 반환
        return {"filtered_influencers": influencers}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        conn.close()

# FastAPI 서버 실행 시 명령어: uvicorn 파일명:app --reload
