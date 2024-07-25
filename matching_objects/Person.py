class Person:
    def __init__(self,email,preferences =[]):
        self.email = email
        self.order_preferences = preferences

    def __str__(self):
        return type(self).__name__ + f"[email={self.email},preferences={self.order_preferences}]"