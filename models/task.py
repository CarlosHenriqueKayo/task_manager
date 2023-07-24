from datetime import datetime

class Task:
    def __init__(self, user_id: int, title: str, description: str, status: str, created_at: datetime):
        self.user_id = user_id 
        self.title = title 
        self.description = description 
        self.status = status 
        self.created_at = created_at
       