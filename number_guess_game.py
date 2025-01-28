import random

def main():
    random_number = random.randint(0, 100)
    win = False
    count = 1
    while(win == False):
        user_number = input("Guess my number from 0-100 >>> ")
        try:
            user_number = int(user_number)
        except:
            print("'", user_number, "'", "is not an acceptable input. Try again.")
        else:
            if(user_number == random_number):
                print("Good guess! My number was indeed", random_number, ". You guessed in", count, "tries. New Game!")
                win = True
            elif(user_number <= random_number):
                print("Too small! Try again!")
                count += 1
            elif(user_number >= random_number):
                print("Too big! Try again!")
                count += 1
                

while True:
    main()
