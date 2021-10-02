import math
import random


# issue1 and 2
class Person:
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


# issue 3
def match(mentors, mentees):
    random.shuffle(mentors)
    random.shuffle(mentees)
    _matches = {}
    _unmatched = []
    m_mentors = []
    f_mentors = []
    for _mentor in mentors:
        if _mentor.gender == 'male':
            m_mentors.append(_mentor)
        elif _mentor.gender == 'female':
            f_mentors.append(_mentor)
        _matches.update({_mentor: []})
    m_mentees = 0
    f_mentees = 0
    for _mentee in mentees:
        if _mentee.gender == 'male':
            m_mentees += 1
        elif _mentee.gender == 'female':
            f_mentees += 1
    max_male = math.ceil(m_mentees / len(m_mentors))
    max_female = math.ceil(f_mentees / len(f_mentors))
    m = 1
    f = 1
    for _mentee in mentees:
        if _mentee.gender == 'male':
            if len(_matches[m_mentors[(m % len(m_mentors)) - 1]]) < max_male:
                _matches[m_mentors[(m % len(m_mentors)) - 1]].append(_mentee)
                m += 1
            else:
                _unmatched.append(_mentee)
        elif _mentee.gender == 'female':
            if len(_matches[f_mentors[(f % len(f_mentors)) - 1]]) < max_female:
                _matches[f_mentors[(f % len(f_mentors)) - 1]].append(_mentee)
                f += 1
            else:
                _unmatched.append(_mentee)
    return [_matches, _unmatched]


if __name__ == '__main__':

    # Collecting mentors info
    mentor_number = int(input("number of mentors: "))
    mentor_list = []
    print("   NAME GENDER(M/F) CONTACT")
    while len(mentor_list) != mentor_number:
        temp = input(f"{len(mentor_list) + 1}: ").split(" ")
        mentor = Person(temp[0], temp[1], temp[2])
        mentor_list.append(mentor)

    # Collecting mentees info
    mentee_number = int(input("number of mentees: "))
    mentee_list = []
    print("   NAME GENDER(M/F) CONTACT")
    while len(mentee_list) != mentee_number:
        temp = input(f"{len(mentee_list) + 1}: ").split(" ")
        mentee = Person(temp[0], temp[1], temp[2])
        mentee_list.append(mentee)
    
    # Getting match results and display
    results = match(mentor_list, mentee_list)
    matches = results[0]
    unmatched = results[1]
    for match in matches:
        temp = ''
        for temp1 in matches[match]:
            temp += f'{temp1.name} {temp1.gender}, '
        print(f'{match.name} {match.gender}: {temp}')
    print(' ')
    temp = ''
    for unmatch in unmatched:
        temp += f'{unmatch.name} {unmatch.gender} ,'
    print(temp)