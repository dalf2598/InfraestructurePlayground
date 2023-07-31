from managers.student_manager import StudentManager


class StudentController:

    @classmethod
    def get_all(cls):
        return StudentManager.get_all()
    
    @classmethod
    def create_student(cls, student):
        return StudentManager.create_student(student)

    @classmethod
    def get_student_by_name(cls, name):
        return StudentManager.get_student_by_name(name) 
    
    @classmethod
    def update_student(cls, student_id, student):
        return StudentManager.update_student(student_id, student)
    
    @classmethod
    def delete_student(cls, student_id):
        return StudentManager.delete_student(student_id)