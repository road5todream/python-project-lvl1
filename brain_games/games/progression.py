from random import randint


TASK = 'What number is missing in the progression?'


def create_progression(start = 0, difference = 0, lenght = 0):
    if start == 0 and difference == 0 and lenght == 0:
        start = randint(1, 100)
        difference = randint(1, 20)
        lenght = randint(5, 10) 
    finish = start + difference * lenght
    progression = []
    while start <= finish:
        progression.append(str(start))
        start += difference
    return progression


def generate_round():
    progression = create_progression()
    hiden_number = randint(0, len(progression) - 1)
    correct_answer = progression[hiden_number]
    for i in range(0, len(progression)):
        if hiden_number == 0:
            progression[0] = '..'
        if i == hiden_number:
            progression[i] = '..'
    question = ('Question: ' + ' '.join(progression))
    question_correct_answer = (question, correct_answer)          
    return question_correct_answer
