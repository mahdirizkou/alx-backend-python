import sqlite3 
import functools

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        conn = sqlite3.connect('users.db')
        try:
            func(conn,*args,**kwargs)
        finally:
            conn.close()          
    """ your code goes here""" 

def transactional(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()  
            return result
        except Exception as e:
            conn.rollback()  
            print(f" if failed change{e}")
            raise  
    return wrapper

@with_db_connection 
@transactional
def get_user_by_id(conn, user_id): 
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)) 
    return cursor.fetchone() 
#### Fetch user by ID with automatic connection handling 

user = get_user_by_id(user_id=1)
print(user)
