import mysql.connector
from mysql.connector import Error


def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',
            password='your_password'  # Replace with your MySQL password
        )

        if connection.is_connected():
            print("Connected to MySQL Server")

            # Create a cursor object
            cursor = connection.cursor()

            # SQL query to create database
            create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"

            # Execute the query
            cursor.execute(create_db_query)

            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if cursor and cursor.is_connected():
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
        print("MySQL connection closed")


if __name__ == "__main__":
    create_database()
