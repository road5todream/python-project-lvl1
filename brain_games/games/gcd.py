from random import randint


TASK = 'Find the greatest common divisor of given numbers.'


def generate_round():
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    question = ('Question: ' + str(random_number1) + ' ' + str(random_number2))
    divisor = 0
    for i in range(1, random_number1 + 1):
        if random_number1 % i == 0:
            if random_number2 % i == 0:
                divisor = max(i, divisor)
                correct_answer = str(divisor)
    question_correct_answer = (question, correct_answer)
    return question_correct_answer
