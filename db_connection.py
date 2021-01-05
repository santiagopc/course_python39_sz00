import psycopg2

db = {
        "dbname": "postgres",
        "port": "5432",
        "host": "localhost",
        "user": "postgres",
        "password": "postgres"
    }
connection1 = psycopg2.connect(**db)
