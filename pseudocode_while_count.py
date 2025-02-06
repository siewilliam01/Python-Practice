while True:
    user_input = input("Enter an integer greater than 20 >>> ")
    try:
        user_integer = int(user_input)
        if(user_integer <= 20):
            raise
    except:
        print("That was not an integer greater than 20, try again.")
    else:
        count = 0
        while(user_integer > 1):
            user_integer /= 2
            count += 1
            print(user_integer)
        print("end")
