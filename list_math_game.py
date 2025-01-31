import random

print("Annoying(and maybe not techincally solvable idk i haven't checked) math game! Fill in the blanks! All are single digit.")

while True:
    win = False
    count = 1
    list_one = []
    list_two = []
    list_three = []
    for i in range(10):
        list_one.append(random.randint(0, 9))
    list_one.sort()
    print(list_one)
    for i in range(5):
        list_two.append(list_one[2*i])
        list_two.append('_')
    print("The sum of", list_two, "=", sum(list_one))
    for i in range(5):
        list_three.append(list_one[2*i+1])
    y = int(''.join(map(str, list_three)))
    while(win == False):
        x = input("Type the missing numbers in a single string >>> ")
        try:
            x = int(x)
        except:
            print(x, "is not a valid input, try again.")
        else:
            if(x == y):
                print("Nice! You won in ", count, "tries. New game!")
                
                win = True
            else:
                print("nope")
                count += 1