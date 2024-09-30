<<<<<<< HEAD
=======
#랭체인을 쓰지 않고 구현한 추천 모델 파일입니다. 아마 해당 파일로 
>>>>>>> d8c5ab6e5ad6990ef214a6566644f26e7ff75441
import openai
import psycopg2
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
<<<<<<< HEAD
import os  # 환경변수 가져오기 위해 os 모듈 사용

=======
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()
>>>>>>> d8c5ab6e5ad6990ef214a6566644f26e7ff75441
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

# PostgreSQL 연결 함수
def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

# 필터링된 인플루언서 추천 (1차 필터링)
@app.post("/recommend")
async def recommend_influencers(filters: FilterRequest):
    try:
        # DB 연결
        conn = get_db_connection()
        cursor = conn.cursor()

        # 필터링된 인플루언서 데이터 조회 (정량적 필터 + 해시태그)
        query = """
        SELECT i.name, i.profile_picture_url, i.biography FROM influencer i
        JOIN meta m ON i.influencer_id = m.influencer_id
        JOIN 미디어_해시태그 mh ON mh.media_id = i.influencer_id
        WHERE i.category = %s
        AND m.follower_cnt BETWEEN %s AND %s
        AND i.gender = %s
        AND mh.hash_tag_id = ANY(%s);
        """
        cursor.execute(query, (filters.category, filters.min_followers, filters.max_followers, filters.gender, filters.keywords))
        influencers = cursor.fetchall()

        # 1차 필터링된 인플루언서 리스트 반환
        return {"db_recommendations": influencers}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cursor.close()
        conn.close()

# 2차 필터링을 위한 GPT와의 대화
@app.post("/final_recommendation")
async def final_recommendation(filters: FilterRequest, business_input: str):
    try:
        # 1차 필터링된 인플루언서 리스트 불러오기
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
        SELECT i.name, i.profile_picture_url, i.biography FROM influencer i
        JOIN meta m ON i.influencer_id = m.influencer_id
        JOIN 미디어_해시태그 mh ON mh.media_id = i.influencer_id
        WHERE i.category = %s
        AND m.follower_cnt BETWEEN %s AND %s
        AND i.gender = %s
        AND mh.hash_tag_id = ANY(%s);
        """
        cursor.execute(query, (filters.category, filters.min_followers, filters.max_followers, filters.gender, filters.keywords))
        influencers = cursor.fetchall()

        # GPT 대화로 추가 필터링 진행
        gpt_prompt = f"광고주가 원하는 카테고리는 {filters.category}이며, 해시태그는 {filters.keywords}입니다. 추가 요구사항: {business_input}. 이에 맞는 상위 인플루언서를 추천해주세요."

        gpt_response = openai.Completion.create(
            engine="gpt-4o-mini",  # GPT-4o mini 모델 사용
            prompt=gpt_prompt,
            max_tokens=100
        )

        gpt_recommendations = gpt_response.choices[0].text.strip()

        return {"db_recommendations": influencers, "gpt_recommendations": gpt_recommendations}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cursor.close()
        conn.close()
