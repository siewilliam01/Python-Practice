import time


my_list_one = []

def main():
    global x
    print(my_list_one)
    my_list_one.append(x)
    x = x + 1
    time.sleep(1)
while True:
    main()