import random

def main():
    flag = True
    while flag:
        num = input('Enter a number: ')

        if num.isdigit():
            print('Lets play!')
            num = int(num)
            flag = False
        else:
            print('Invalid digit... Try again!')

    r1 = random.randint(1,num)

    guess = None
    count = 1

    while guess != r1:
        guess = input('Please type a number between 1 and '+ str(num)+ ': ')
        if guess.isdigit():
            guess = int(guess)

        if guess == r1:
            print('You got it!')
        else:
            print('Try again!')
            count += 1

    print('It took you',count, 'guesses!')

    repeat = input('Do you want to play again? (y/n): ').lower()
    if repeat != 'y':
        print('Bye')
        exit()
    else:
        main()

main()