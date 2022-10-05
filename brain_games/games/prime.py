from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    number_of_divisors = 0
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            number_of_divisors += 1
    if number_of_divisors == 0:
        return True
    else:
        return False


def generate_round():
    random_number = randint(1, 100)
    question = ('Question: ' + str(random_number))
    if is_prime(random_number) is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question_correct_answer = (question, correct_answer)      
    return question_correct_answer
