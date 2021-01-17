import psycopg2

try:
    db = {
        "dbname": "postgres",
        "port": "5432",
        "host": "localhost",
        "user": "martin",
        "password": "1598753228046"
    }
    connection1 = psycopg2.connect(**db)
    print(f"todo salio bien {connection1}")

    print("first select your favorite comic book house:")
    print("marvel")
    print("dc_comics")

    elect = input("chose your favorite comics house: ")

    if elect == "marvel":
        with connection1.cursor() as cursor:
            cursor.execute("SELECT * FROM marvel")
            superheros = cursor.fetchall()

            for superheros in superheros:
                print("{}".format(superheros))

    if elect == "dc_comics":
        with connection1.cursor() as cursor:
            cursor.execute("SELECT * FROM dc_comics")
            superheros = cursor.fetchall()

            for superheros in superheros:
                print("{}".format(superheros))

    if elect == "Select ":
        with connection1.cursor() as cursor:
            cursor.execute("SELECT * FROM marvel")
            superheros = cursor.fetchall()

            for superheros in superheros:
                print("{}".format(superheros))

    cursor = connection1.cursor()

    create_hero = ['name', 'last_name', 'super_name', 'alias', 'autor', 'first_apparation', 'year_of_creation', 'comics_house']
    create_user = "INSERT INTO accounts ('username', 'password', 'email') VALUES (%s, %s, %s)"
    name = input("Escribe tu nombre: ")
    password = input("Escribe tu contraseña: ")
    email = input("Escribe tu email: ")
    user_account = (name, password, email)
    cursor.execute(create_user, user_account)

    connection1.commit()
    count = cursor.rowcount
    print(count, "Esto fue lo que se guardo")

except:
    print("Nada salio bien")
