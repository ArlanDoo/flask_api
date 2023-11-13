import datetime

class Post:
    
    def __init__(self, author: str, description: str,
                 date_add = datetime.datetime.now(),
                 date_update = datetime.datetime.now()):
        
        self.author = author
        self.description = description
        self.added = date_add
        self.update = date_update