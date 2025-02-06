while True:
    user_input = input("enter int from 0-9 >>> ")
    try:
        user_int = int(user_input)
        if(user_int < 0 or user_int > 9):
            raise
    except:
        print("not an int between 0 and 9, try again")
    else:
        print(user_int)
        print("starting while loop")
        count = 0
        while(count < 10):
            if(user_int == count):
                print("user variable equals the count variable")
                print("User =", user_int)
                print("Count =", count)
            else:
                print(count)
            count += 1
        print("end")