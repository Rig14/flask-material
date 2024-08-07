import psycopg
from flask import current_app


def create_user(name: str, password: str):
    with psycopg.connect(current_app.config["POSTGRES_CONNECTION_STRING"]) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO users (name, password) VALUES (%s, %s)",
                (name, password)
            )
            conn.commit()

def check_user(name: str, password: str):
    with psycopg.connect(current_app.config["POSTGRES_CONNECTION_STRING"]) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, password FROM users WHERE name = %s",
                (name,)
            )
            user_data = cur.fetchone()
            if user_data and password == user_data[1]:
                return user_data[0]
            return None