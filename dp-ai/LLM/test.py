import psycopg2

# PostgreSQL 연결 설정
DB_HOST = "postgresql-db.cb2u2kg2clg0.ap-northeast-2.rds.amazonaws.com"
DB_NAME = "postgres"
DB_USER = "root"
DB_PASSWORD = "WHDgkqtjfrP!"

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
