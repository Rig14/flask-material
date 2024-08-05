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
