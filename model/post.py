import datetime
from psycopg2 import Error
from postgres.create_db import connection_to_db

class Post:
    
    def __init__(self, id: int, author: str, description: str,
                 rating: int, added: str, updated: str):
        
        self.id = id
        self.author = author
        self.description = description
        self.rating = rating if rating else 0
        self.added = added if added else datetime.datetime.now()
        self.updated = updated if updated else datetime.datetime.now()


    def get_post(self):
        
        try:
            
            cursor = connection_to_db()
            
            cursor.execute("""
                SELECT * FROM posts
                WHERE id=%(id)s and author=%(author)s;
                """,
                {"id": self.id, "author": self.author})
            
            result = cursor.fetchall()
            
            if (len(result)):
                return result
            else:
                return {
                    "response": "Post is not fined"
                }
        
        except Error as err:
            
            return ({
                "error": err
            })
    
    
    def delete_post(self):
        
        try:
            
            cursor = connection_to_db()
            
            cursor.execute("""
                DELETE FROM posts WHERE id=%(id)s;
                """,
                {"id": self.id})
            
            return {"response": "Post deleted"}
        
        except Error as err:
            
            return ({
                "error": err
            })
    
        
    def add_post(self):
        
        try:
            
            cursor = connection_to_db()
            
            cursor.execute("""
                INSERT INTO posts (id, author, description, rating, added, updated)
                VALUES (%(id)s, %(author)s, %(desc)s, %(rating)s, %(add)s, %(upd)s);
                """,
                {"id": self.id, "author": self.author, "desc": self.description,
                "rating": self.rating, "add": self.added, "upd": self.updated})
            
            cursor.close()
            
            return ({
                    "response": "Post is success added"
                })
        
        except Error as err:
            
            return ({
                "error": err
            })


    def update_post(self):
        
        try:
            
            cursor = connection_to_db()
            
            cursor.execute("""
                UPDATE posts
                SET description = %(desc)s, rating = %(rating)s, updated = %(upd)s
                WHERE id = %(id)s;
                """,
                {"id": self.id, "author": self.author, "desc": self.description,
                "rating": self.rating, "upd": self.updated})
            
            cursor.close()
            
            return ({"response": "Post is success update"})
        
        except Error as err:
            
            return ({
                "error": err
            })