import random

def main():
    random_number = random.randint(0, 9)
    win = False
    while(win == False):
        user_number = input("Guess my number from 0-9 >>> ")
        try:
            user_number = int(user_number)
        except:
            print("'", user_number, "'", "is not an acceptable input. Try again.")
        else:
            if(user_number == random_number):
                print("Good guess! My number was indeed", random_number, ". New Game!")
                win = True
            else:
                print("Wrong! Try Again!")

while True:
    main()