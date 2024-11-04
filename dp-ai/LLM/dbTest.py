import psycopg2
from dotenv import load_dotenv
import os

# .env 파일에서 환경 변수 로드
load_dotenv()

# PostgreSQL 연결 설정 (환경 변수에서 로드)
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# PostgreSQL 연결 함수
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        print("PostgreSQL 데이터베이스에 성공적으로 연결되었습니다.")
        return conn
    except Exception as e:
        print(f"데이터베이스 연결 실패: {e}")
        return None

# 연결 테스트
if __name__ == "__main__":
    conn = get_db_connection()
    if conn:
        conn.close()
        print("연결이 정상적으로 종료되었습니다.")
