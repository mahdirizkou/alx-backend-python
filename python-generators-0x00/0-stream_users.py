import mysql.connector

def stream_users():
    """Yields users one by one from user_data table using a generator"""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='ALX_prodev'
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")

        for row in cursor:
            yield row  # Generator yields one row at a time

        cursor.close()
        connection.close()

    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")
