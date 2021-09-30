# issue 1
class Mentor:
    def __init__(self, name, gender, contact):
        self.name = name
        self.contact = contact
        if gender == 'M':
            self.gender = 'male'
        else:
            self.gender = 'female'

    def name(self):
        return self.name

    def gender(self):
        return self.gender

    def contact(self):
        return self.contact


# issue 2
class Mentee:
    def __init__(self, name, gender, contact):
        self.name = name
        self.contact = contact
        if gender == 'M':
            self.gender = 'male'
        else:
            self.gender = 'female'

    def name(self):
        return self.name

    def gender(self):
        return self.gender

    def contact(self):
        return self.contact


