from random import choice
from random import randint


TASK = 'What is the result of the expression?'


def generate_round():
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    random_number3 = choice('+-*')
    question = ('Question: ' + str(random_number1) + ' '
                + random_number3 + ' ' + str(random_number2))
    if random_number3 == '+':
        correct_answer = str(random_number1 + random_number2)
    elif random_number3 == '-':
        correct_answer = str(random_number1 - random_number2)
    else:
        correct_answer = str(random_number1 * random_number2)
    question_correct_answer = (question, correct_answer)
    return question_correct_answer
