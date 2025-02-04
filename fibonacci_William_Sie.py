import time
import random

my_fib = []
fib_int1 = 0
fib_int2 = 0

def startup():
    global my_fib
    global fib_int1
    global fib_int2
    my_fib = []
    fib_int1 = 0
    fib_int2 = 0

def ask():
    global fib_int1
    input_correct = False
    while(input_correct == False):
        fib_int1 = input("Input an integer from 0-9 >>> ")
        try:
            fib_int1 = int(fib_int1)
            if(fib_int1 > 9 or fib_int1 < 0):
                raise
        except:
            print(fib_int1, "is not an integer from 0-9, try again.")
        else:
            input_correct = True
    print("You have input", fib_int1, "as your integer.")
    
def random_generator():
    global fib_int2
    fib_int2 = random.randint(1, 20)
    print("The computer has randomly chosen", fib_int2)
    
def start_sequence():
    my_fib.append(fib_int1)
    my_fib.append(fib_int2)
    print(my_fib)
    
def repeat_sequence():
    for i in range(10):
        time.sleep(0.1)
        my_fib.append(my_fib[-1] + my_fib[-2])
        print(my_fib)

while True:
    startup()
    ask()
    random_generator()
    start_sequence()
    repeat_sequence()
    print(my_fib, "Done.")

