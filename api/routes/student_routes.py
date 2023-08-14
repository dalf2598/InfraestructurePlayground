from typing import Optional
from fastapi import APIRouter
from controllers.student_controller import StudentController
from models.student import Student

router = APIRouter()

@router.get("/")
def get_all():
    return StudentController.get_all()

@router.post("/create-student")
def create_student(student: Student):
    return StudentController.create_student(student)

@router.get("/get-by-name")
def get_student_by_name(name: Optional[str] = None):
    return StudentController.get_student_by_name(name)

@router.put("/update-student/{student_id}")
def post_student(student_id: int, update_student: Student):
    return StudentController.update_student(student_id, update_student)

@router.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    return StudentController.delete_student(student_id)

#Hello