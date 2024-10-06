import openai
import psycopg2
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()
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

# 1차 필터링: 정량적 데이터를 이용한 인플루언서 추천
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

        return {"db_recommendations": influencers}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cursor.close()
        conn.close()

# 2차 GPT와 대화하며 추가 필터링 (LangChain 사용)
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

        # LangChain으로 GPT 대화 진행
        llm = OpenAI(model="gpt-4o")  # GPT 모델 설정

        # 프롬프트 템플릿을 정의
        prompt = PromptTemplate(
            input_variables=["category", "keywords", "business_input"],
            template="광고주는 {category} 카테고리에서 {keywords} 키워드를 원합니다. 추가 요구사항은 {business_input}입니다. 추천할 인플루언서를 나열해 주세요."
        )

        # LLM Chain 설정
        chain = LLMChain(llm=llm, prompt=prompt)

        # LLM에 요청해서 추가 필터링 진행
        gpt_recommendations = chain.run({
            "category": filters.category,
            "keywords": ", ".join(filters.keywords),
            "business_input": business_input
        })

        return {"db_recommendations": influencers, "gpt_recommendations": gpt_recommendations}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cursor.close()
        conn.close()
