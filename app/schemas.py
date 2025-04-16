from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CreateTask(BaseModel):
    # video_url:str
    task_type:str
    

class ResponseTask(BaseModel):
    id:int
    video_url:str
    task_type:str
    status:str
    result:Optional[str]
    created_at:datetime 