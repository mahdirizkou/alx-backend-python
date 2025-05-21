import mysql.connector

def stream_users_in_batches(batch_size):
    """Yields batches of users from the user_data table"""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='your_mysql_user',
            password='your_mysql_password',
            database='ALX_prodev'
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")

        batch = []
        for row in cursor:
            batch.append(row)
            if len(batch) == batch_size:
                yield batch
                batch = []
        if batch:
            yield batch

        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")

def batch_processing(batch_size):
    """Processes batches and filters users over age 25"""
    for batch in stream_users_in_batches(batch_size):
        filtered = [user for user in batch if user['age'] > 25]
        yield filtered
