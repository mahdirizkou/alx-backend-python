import mysql.connector
from mysql.connector import Error


def stream_user_ages():
    """
    Generator function that yields user ages one by one from the database.
    Uses yield to provide ages without loading all data into memory at once.
    
    Yields:
        int: Age of each user, one at a time
    """
    try:
        
        seed = __import__('seed')
        
       
        connection = seed.connect_to_prodev()
        
        if connection:
            cursor = connection.cursor()
            
            cursor.execute("SELECT age FROM user_data")
            for (age,) in cursor:
                yield age
            cursor.close()
            connection.close()
    
    except Error as e:
        print(f"Error streaming ages: {e}")


def calculate_average_age():
    """
    Calculates the average age of users using the stream_user_ages generator.
    Memory-efficient as it only holds running total and count, not all ages.
    
    Returns:
        float: The average age of all users
    """
    total_age = 0
    count = 0
    for age in stream_user_ages():
        total_age += age
        count += 1
    if count > 0:
        return total_age / count
    else:
        return 0


if __name__ == "__main__":
    avg_age = calculate_average_age()
    print(f"Average age of users: {avg_age:.2f}")