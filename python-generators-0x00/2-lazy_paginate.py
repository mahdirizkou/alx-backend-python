import mysql.connector
from mysql.connector import Error


def paginate_users(page_size, offset):
    """
    Function to fetch paginated user data from the database.
    
    Args:
        page_size (int): Number of records per page
        offset (int): Starting position for fetching records
        
    Returns:
        list: A list of user dictionaries for the requested page
    """
    try:
        
        seed = __import__('seed')
        
        connection = seed.connect_to_prodev()
        
        if connection:
            cursor = connection.cursor(dictionary=True)
            
          
            cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
            
           
            rows = cursor.fetchall()
            
            
            cursor.close()
            connection.close()
            
            return rows
            
    except Error as e:
        print(f"Error fetching paginated data: {e}")
        return []


def lazy_pagination(page_size):
    """
    Generator function that implements lazy loading of paginated data.
    Uses yield to return each page only when needed.
    
    Args:
        page_size (int): Number of records per page
        
    Yields:
        list: A page of user data (list of dictionaries)
    """
   
    offset = 0
    
    
    while True:
        
        current_page = paginate_users(page_size, offset)
        
        
        if not current_page:
            break
        
   
        yield current_page
        
      
        offset += page_size


if __name__ == "__main__":
    
    for i, page in enumerate(lazy_pagination(10)):
        print(f"Page {i+1}:")
        for user in page:
            print(f"  {user['name']} ({user['email']})")
        
        
        if i >= 2:
            break