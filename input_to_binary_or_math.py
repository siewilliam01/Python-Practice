while True:
    user_input = input("input anything >>> ")
    try:
        user_input = int(user_input)
    except:
        user_input = str(user_input)
    print(user_input)
    if(type(user_input) == str):
        user_binary = ""
        for i in range(len(user_input)):
            character_binary = bin(ord(user_input[i]))[2:]
            user_binary += (character_binary.rjust(8, "0") + " ")
        print("In binary that is", user_binary)
    elif(type(user_input) == int):
        user_input = abs(user_input)
        user_divide = user_input / 3.1415926
        print(user_divide)