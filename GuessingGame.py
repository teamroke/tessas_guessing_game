import random

def guessinggame():
    numbertoguess = random.randint(1,100)
    keepgoing = True
    print('Guess the number between 1 and 100. Enter q to quit.')
    while keepgoing:
        guess = input('Guess the number: ')
        if guess == 'q':
            keepgoing = False
        else:
            try:
                guess = int(guess)
                if guess >= 1 and guess <= 100:
                    if guess < numbertoguess:
                        print('Too low!')
                    elif guess > numbertoguess:
                        print('Too high!')
                    elif guess == numbertoguess:
                        print('You win!')
                        keepgoing = False
                else:
                    print('The number has to be between 1 and 100, dummy.')
            except:
                print('Enter a number, silly.')
        

if __name__ == '__main__':
    guessinggame()