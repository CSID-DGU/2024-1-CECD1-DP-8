import openai
import psycopg2
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import numpy as np

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

# RWR 알고리즘 구현
def rwr(weighted_edges, seed_node, restart_prob=0.15, max_iters=100, tol=1e-6):
    """
    Random Walk with Restart 알고리즘을 이용하여 특정 노드와 연관이 있는 노드들을 필터링
    """
    nodes = set()
    for edge in weighted_edges:
        nodes.add(edge[0])
        nodes.add(edge[1])
    nodes = list(nodes)
    n = len(nodes)
    
    node_to_index = {node: i for i, node in enumerate(nodes)}
    
    transition_matrix = np.zeros((n, n))
    for edge in weighted_edges:
        i = node_to_index[edge[0]]
        j = node_to_index[edge[1]]
        transition_matrix[j, i] = float(edge[2])
    
    for i in range(n):
        col_sum = np.sum(transition_matrix[:, i])
        if col_sum > 0:
            transition_matrix[:, i] /= col_sum

    restart_vector = np.zeros(n)
    restart_vector[node_to_index[seed_node]] = 1

    scores = np.zeros(n)
    scores[node_to_index[seed_node]] = 1

    for _ in range(max_iters):
        prev_scores = np.copy(scores)
        scores = restart_prob * np.dot(transition_matrix, scores) + (1 - restart_prob) * restart_vector
        if np.linalg.norm(scores - prev_scores, ord=1) < tol:
            break
    
    ranked_nodes = sorted(zip(nodes, scores), key=lambda x: x[1], reverse=True)
    return ranked_nodes

# 1차 필터링 함수 (연관 해시태그 기반 필터링된 인플루언서)
def get_influencers_by_hashtags(weighted_edges, seed_hashtag, conn):
    ranked_hashtags = rwr(weighted_edges, seed_hashtag)
    top_hashtags = [node for node, score in ranked_hashtags[:10]]  # 상위 10개의 연관 해시태그
    
    cursor = conn.cursor()
    
    # 필터링된 해시태그를 바탕으로 인플루언서 조회
    query = """
    SELECT i.name, i.profile_picture_url, i.biography 
    FROM influencer i
    JOIN meta m ON i.influencer_id = m.influencer_id
    JOIN media me ON me.influencer_id = i.influencer_id
    WHERE me.caption LIKE ANY(%s);
    """
    cursor.execute(query, (top_hashtags,))
    influencers = cursor.fetchall()
    
    return influencers

# 1차 필터링 (정량적 데이터 + 해시태그 기반)
@app.post("/recommend")
async def recommend_influencers(filters: FilterRequest):
    try:
        conn = get_db_connection()
        
        # 해시태그 기반 필터링된 인플루언서 목록을 가져옴
        weighted_edges = [
            # 간단한 예시. 실제로는 해시태그와 그 가중치를 반영한 데이터를 넣어야 함.
            ('#fashion', '#summer', 0.5),
            ('#summer', '#beach', 0.7),
            ('#fashion', '#style', 0.8),
            ('#beach', '#vacation', 0.6)
        ]
        seed_hashtag = filters.keywords[0]  # 첫 번째 키워드를 기준으로 필터링
        influencers = get_influencers_by_hashtags(weighted_edges, seed_hashtag, conn)

        # 필터링된 인플루언서 리스트 반환
        return {"filtered_influencers": influencers}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        conn.close()