import psycopg
from flask import current_app


def log_search_query(user_id, lat, lon):
    with psycopg.connect(current_app.config["POSTGRES_CONNECTION_STRING"]) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO history_entries (lat, lon, user_id) VALUES (%s, %s, %s)",
                (lat, lon, user_id)
            )
            conn.commit()


def get_user_search_histroy(user_id):
    with psycopg.connect(current_app.config["POSTGRES_CONNECTION_STRING"]) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT lat, lon FROM history_entries WHERE user_id = %s",
                (user_id,)
            )
            history = cur.fetchall()
            return history
