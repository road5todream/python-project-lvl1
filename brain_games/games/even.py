from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    random_number = randint(1, 1000000000)
    question = ('Question: ' + str(random_number))
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question_correct_answer = (question, correct_answer) 
    return question_correct_answer
