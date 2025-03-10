from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Task
from app.schemas import TaskCreate, Task
from app.services.task_service import (
    create_new_task,
    get_task,
    update_existing_task,
    delete_task,
)
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=Task)  # Usa Task directamente desde app.schemas
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_new_task(db, task)

@router.get("/{task_id}", response_model=Task)  # Usa Task directamente desde app.schemas
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = get_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=Task)  # Usa Task directamente desde app.schemas
def update_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    return update_existing_task(db, task_id, task)

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return delete_task(db, task_id)