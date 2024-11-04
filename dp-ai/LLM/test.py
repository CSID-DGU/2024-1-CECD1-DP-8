import psycopg2
import os  # 환경변수 가져오기 위해 os 모듈 사용
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()
# PostgreSQL 연결 설정 - 환경변수에서 값 가져오기
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# PostgreSQL 연결 함수
def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

# DB 연결 확인 함수
def check_db_connection():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1;")
        result = cursor.fetchone()
        print("DB 연결 성공: ", result)
    except Exception as e:
        print("DB 연결 실패: ", e)
    finally:
        cursor.close()
        conn.close()

# 메인 함수
if __name__ == "__main__":
    check_db_connection()
