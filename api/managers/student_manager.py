from typing import Optional
from models.student import Student


class StudentManager:
    students = {
        1: {
            "name": "diego",
            "age": 24,
        },
        2: {
            "name": "david",
            "age": 25,
        },
    }

    @classmethod
    def get_all(cls):
        return cls.students

    @classmethod
    def create_student(cls, student: Student):
        cls.students[len(cls.students) + 1] = student.dict()
        return {"Data": "Created Successfully"}

    @classmethod
    def get_student_by_name(cls, name: Optional[str] = None):
        for student_id in cls.students:
            if cls.students[student_id]["name"] == name:
                return cls.students[student_id]
        return {"Data": "Not Found"}

    @classmethod
    def update_student(cls, student_id: int, update_student: Student):
        if student_id not in cls.students:
            return {"Error": "Student Not Found"}

        if update_student.name:
            cls.students[student_id]["name"] = update_student.name
        if update_student.age:
            cls.students[student_id]["age"] = update_student.age
        return {"message": "Person updated successfully"}

    @classmethod
    def delete_student(cls, student_id: int):
        if student_id not in cls.students:
            return {"Error": "Student Not Found"}
        del cls.students[student_id]
        return {"message": "Person deleted successfully"}
