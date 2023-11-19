from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from postgres.create_db import connection_to_db

class User:
    
    def __init__(self, id: int, firstname: str,
                 lastname: str, age: int, email: str):
        
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.email = email
    
    def add_user(self):
        
        try:
            
            cursor = connection_to_db()
            
            cursor.execute("""
                INSERT INTO users (id, firstname, lastname, age, email)
                VALUES (%(id)s, %(fname)s, %(lname)s, %(age)s, %(email)s);
                """,
                {"id": self.id, "fname": self.firstname, "lname": self.lastname, "age": self.age, "email": self.email})
            
            cursor.close()
            
            return ({"response": "User is success added"})
        
        except Error as err:
            
            return ({
                "error": err
            })