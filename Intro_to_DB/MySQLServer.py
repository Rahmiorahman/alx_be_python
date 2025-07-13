import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None  # Initialize connection
    try:
        # Connect to MySQL server (adjust user/password/host as needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"  # Replace with your actual password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create the database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")


if __name__ == "__main__":
    create_database()
