import pymysql
import bcrypt

def connect_to_database(host, user, password, database):
    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except pymysql.MySQLError as e:
        print(f"Error connecting to database: {e}")
        return None

def create_admin_user(connection):
    try:
        cursor = connection.cursor()
        username = "admin"
        plain_password = "1234"
        hashed_password = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        role = "admin"

        query = "INSERT INTO users (username, password_hash, role) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, hashed_password, role))
        connection.commit()
        cursor.close()
        print(f"Admin user created with username: {username} and password: {plain_password}")
    except pymysql.MySQLError as e:
        print(f"Error creating admin user: {e}")

if __name__ == "__main__":
    connection = connect_to_database("localhost", "root", "1234", "login_system_umrechner")
    if connection:
        create_admin_user(connection)
        connection.close()
    else:
        print("Failed to connect to the database.")
