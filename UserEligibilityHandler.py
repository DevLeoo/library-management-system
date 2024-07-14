class UserEligibilityHandler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, request):
        if request.user.is_eligible():
            if self.next_handler:
                return self.next_handler.handle(request)
            return True
        else:
            return "User cannot rent books"
