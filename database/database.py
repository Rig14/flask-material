import os.path

import psycopg
from flask import current_app


def create_database():
    # load schema.sql file into variable
    schema: str
    with open(os.path.join(os.path.abspath("."), "database", "schema.sql"), "r") as file:
        schema = file.read()

    # Connect to an existing database
    with psycopg.connect(current_app.config["POSTGRES_CONNECTION_STRING"]) as conn:
        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            # Execute the schema script to initialize the database
            cur.execute(schema)
            # Commit the changes to the database
            # When this is not called, no changes will be made to database.
            conn.commit()
