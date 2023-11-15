import datetime

class Post:
    
    def __init__(self, post_id: int, author: str, description: str,
                 date_add = datetime.datetime.now(),
                 date_update = datetime.datetime.now()):
        
        self.post_id = post_id
        self.author = author
        self.description = description
        self.date_add = str(datetime.timedelta(date_add))
        self.date_update = str(datetime.timedelta(date_update))