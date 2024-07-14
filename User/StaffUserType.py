from . import User

class StaffUserType(User):
    def is_eligible(self, operation):
        return False # nao pode alugar
        