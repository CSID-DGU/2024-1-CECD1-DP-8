import psycopg2

from config import PostgresConfig


def get_db_connection():
    conn = psycopg2.connect(
        dbname=PostgresConfig.dbname,
        user=PostgresConfig.user,
        password=PostgresConfig.password,
        host=PostgresConfig.host,
        port=PostgresConfig.port
    )
    cur = conn.cursor()
    return conn, cur
