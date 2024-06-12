import pymysql
import bcrypt

#===== Connect to Database =====
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

#===== Verify Login =====
def verify_login(connection, username, password):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()
        cursor.close()
        
        if user:
            stored_password = user['password_hash']
            
            # Check if the stored password is already hashed with bcrypt
            if stored_password.startswith('$2b$'):
                if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                    return user
            else:
                # If the password is not hashed, check if it matches the plain text password
                if stored_password == password:
                    # Hash the plain text password and update the database
                    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                    cursor = connection.cursor()
                    cursor.execute("UPDATE users SET password_hash = %s WHERE id = %s", (hashed_password, user['id']))
                    connection.commit()
                    cursor.close()
                    return user
        return None
    except pymysql.MySQLError as e:
        print(f"Error verifying login: {e}")
        return None

#===== Create User =====
def create_user(connection, username, password_hash, role):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO users (username, password_hash, role) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, password_hash.decode('utf-8'), role))
        connection.commit()
        cursor.close()
        return True
    except pymysql.MySQLError as e:
        print(f"Error creating user: {e}")
        return False

#===== Delete User =====
def delete_user(connection, username):
    try:
        cursor = connection.cursor()
        query = "DELETE FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        connection.commit()
        cursor.close()
        return cursor.rowcount > 0  # Returns True if a row was deleted
    except pymysql.MySQLError as e:
        print(f"Error deleting user: {e}")
        return False

#===== Get All Users =====
def get_all_users(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT username, role FROM users"
        cursor.execute(query)
        users = cursor.fetchall()
        cursor.close()
        return users
    except pymysql.MySQLError as e:
        print(f"Error fetching users: {e}")
        return []

#===== Get User Role =====
def get_user_role(connection, username):
    try:
        cursor = connection.cursor()
        query = "SELECT role FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()
        cursor.close()
        return user['role'] if user else None
    except pymysql.MySQLError as e:
        print(f"Error fetching user role: {e}")
        return None

#===== Update User Role =====
def update_user_role(connection, username, new_role):
    try:
        cursor = connection.cursor()
        query = "UPDATE users SET role = %s WHERE username = %s"
        cursor.execute(query, (new_role, username))
        connection.commit()
        cursor.close()
        return cursor.rowcount > 0  # Returns True if a row was updated
    except pymysql.MySQLError as e:
        print(f"Error updating user role: {e}")
        return False

#===== Close Connection =====
def close_connection(connection):
    try:
        if connection and connection.open:
            connection.close()
    except pymysql.MySQLError as e:
        print(f"Error closing connection: {e}")
