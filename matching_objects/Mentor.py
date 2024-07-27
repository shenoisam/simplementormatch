from matching_objects.Person import Person

class Mentor(Person):
    def __init__(self, email,preferences=[]):
        self.mentee_list = []
        self.order_preferences = preferences
        self.email = email
        #super().__init__(email,preferences)
    def __str__(self):
        return type(self).__name__ + f"[email={self.email},preferences={self.order_preferences},mentee_list={len(self.mentee_list)}]"
