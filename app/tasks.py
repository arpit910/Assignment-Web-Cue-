from sqlalchemy.orm import Session
from . import models
import time

def process_video(task_id:int, db:Session):
    task=db.query(models.task).filter(models.task.id==task_id).first()
    task.status="processing"
    db.commit()

    time.sleep(5)

    if(task.task_type=="extract_audio"):
        task.result=f"{task.video_url}_audio.mp3"
    elif(task.task_type=="thumbnail"):
        task.result=f"{task.video_url}_thumb.jpg"
    elif(task.task_type=="compress"):
        task.result=f"{task.video_url}_compressed.mp4"
    else:
        task.result="unknown task"

    task.status="completed"
    db.commit()
    
    
