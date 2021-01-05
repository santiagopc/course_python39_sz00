import db_connection
import psycopg2

cursor = db_connection.connection1
if cursor:
    cursor = psycopg2
    psycopg2.cursor("SELECT * FROM superheros")
    superheros = cursor.fetchall()

    for superheros in superheros:
        print(f"this is my list of data base: {superheros}")
else:
    print("im not read db")
