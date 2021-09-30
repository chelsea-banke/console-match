import builder
import math


# issue 3
def match(mentors, mentees):
    _matches = {}
    _unmatched = []
    m_mentors = []
    f_mentors = []
    for _mentor in mentors:
        if _mentor.gender == 'male':
            m_mentors.append(_mentor)
        else:
            f_mentors.append(_mentor)
        _matches.update({_mentor: []})
    m_mentees = 0
    f_mentees = 0
    for _mentee in mentees:
        if _mentee.gender == 'male':
            m_mentees += 1
        else:
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
        else:
            if len(_matches[f_mentors[(f % len(f_mentors)) - 1]]) < max_female:
                _matches[f_mentors[(f % len(f_mentors)) - 1]].append(_mentee)
                f += 1
            else:
                _unmatched.append(_mentee)
    return [_matches, _unmatched]


if __name__ == '__main__':
    # Collecting mentors
    mentor_number = int(input("number of mentors: "))
    mentor_list = []
    print("NAME GENDER(M/F) CONTACT")
    while len(mentor_list) != mentor_number:
        temp = input(f"{len(mentor_list) + 1}: ").split(" ")
        mentor = builder.Mentor(temp[0], temp[1], temp[2])
        mentor_list.append(mentor)

    # Collecting mentees
    mentee_number = int(input("number of mentees: "))
    mentee_list = []
    print("NAME GENDER(M/F) CONTACT")
    while len(mentee_list) != mentee_number:
        temp = input(f"{len(mentee_list) + 1}: ").split(" ")
        mentee = builder.Mentee(temp[0], temp[1], temp[2])
        mentee_list.append(mentee)

    # matching and display
    matches = match(mentor_list, mentee_list)[0]
    unmatched = match(mentor_list, mentee_list)[1]
    for match in matches:
        temp = []
        for temp1 in matches[match]:
            temp.append(temp1.name)
        print(f'{match.name} --> {temp}')
    temp = []
    for unmatch_ in unmatched:
        temp.append(unmatch_.name)
    if len(temp) > 0:
        print(f'unmatched --> {temp}')
