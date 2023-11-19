import datetime
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

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
        
        cursor = connection_to_db()
        
        cursor.execute("""
            SELECT * FROM posts
            WHERE id=%(id)s and author=%(author)s;
            """,
            {"id": self.id, "author": self.author})
        
        return (cursor.fetchall())
    
    
    def delete_post(self):
        
        cursor = connection_to_db()
        
        cursor.execute("""
            DELETE FROM posts
            WHERE id=%(id)s;
            """,
            {"id": self.id})
        
        return (cursor)
    
        
    def add_post(self):
        
        cursor = connection_to_db()
        
        cursor.execute("""
            INSERT INTO posts (id, author, description, rating, added, updated)
            VALUES (%(id)s, %(author)s, %(desc)s, %(rating)s, %(add)s, %(upd)s);
            """,
            {"id": self.id, "author": self.author, "desc": self.description,
             "rating": self.rating, "add": self.added, "upd": self.updated})
        
        cursor.close()
        
        return ({"response": "Post is success added"})