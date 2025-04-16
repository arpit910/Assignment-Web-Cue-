from sqlalchemy import Column, Integer, String, DateTime
from .database import Base
from datetime import datetime
class task(Base):
    __tablename__="tasks"
    
    id=Column(Integer, primary_key=True, index=True)
    video_url=Column(String,nullable=False)
    task_type=Column(String,nullable=False)
    status=Column(String, default="pending")
    result=Column(String, nullable=True)
    created_at=Column(DateTime,default=datetime.utcnow)
    