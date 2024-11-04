import psycopg2
from psycopg2.extras import RealDictCursor
from config import PostgresConfig


def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname=PostgresConfig.dbname,
            user=PostgresConfig.user,
            password=PostgresConfig.password,
            host=PostgresConfig.host,
            port=PostgresConfig.port
        )
        cur = conn.cursor(cursor_factory=RealDictCursor)    # RealDictCursor: row[3] 대신 row['column']
        print("DB connection success!")
        return conn, cur
    except psycopg2.Error as e:
        print(f"DB connection failed: {e}")
        return None, None
