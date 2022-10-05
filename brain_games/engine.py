import sys
import prompt


ROUNDS = 3


def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + '!')
    print(game.TASK)
    global ROUNDS
    for i in range(ROUNDS):
        question, correct_answer = game.generate_round()
        print(question)
        answer = input('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print("'" + str(answer) + "'"
                  + ' is wrong answer ;(. Correct answer was '
                  + "'" + str(correct_answer) + "'.")
            print("Let's try again, " + name + "!")
            sys.exit()
    print('Congratulations, ' + name + '!')
