import os, shutil
from fastapi import FastAPI, BackgroundTasks, Depends, HTTPException, UploadFile, Form
from . import models, database,schemas, tasks
from sqlalchemy.orm import Session
from typing import List

app=FastAPI()

#Initialize DB
models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db=database.sessionLocal()
    try:
        yield db
    finally:
        db.close()


app.get('/')
def root():
    return{"message":"Welcome"}    



@app.post("/tasks/", response_model=schemas.ResponseTask)
async def create_task(file: UploadFile,task_type: str = Form(...),background_tasks: BackgroundTasks = BackgroundTasks(),
    db: Session = Depends(get_db),
):
   
    os.makedirs("upload", exist_ok=True)
    dst = os.path.join("upload", file.filename)
    with open(dst, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    task = models.task(video_url=file.filename, task_type=task_type)
    db.add(task)
    db.commit()
    db.refresh(task)
    background_tasks.add_task(tasks.process_video, task.id, db)
    db.refresh(task)

    return task



@app.get("/tasks", response_model=List[schemas.ResponseTask])
def get_All_Tasks(db:Session=Depends(get_db)):
    tasks=db.query(models.task).all()
    return tasks



@app.get("/tasks/{id}", response_model=schemas.ResponseTask)
def get_Task_By_Id(task_id:int, db:Session=Depends(get_db)):
    task=db.query(models.task).filter(models.task.id==task_id).first()
    if not task:
        raise HTTPException(status_code=404, details="Task not Found")
    return task


