from . import User

class TeacherUserType(User):
    def is_eligible(self, operation):
        return False # nao pode alugar