from matching_objects.Person import Person

class Mentor(Person):
    def __init__(self, email,preferences=[]):
        super().__init__(email,preferences)
        self.mentee_list = []