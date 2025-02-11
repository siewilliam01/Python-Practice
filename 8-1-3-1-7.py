while True:
    user_in = input("user >>> ")
    bin_string = ""
    hex_string = ""
    chr_string = ""
    for i in range(len(user_in)):
        character_ord = ord(user_in[i])
        character_bin = bin(character_ord)[2:]
        character_hex = hex(character_ord)[2:]
        character_chr = chr(character_ord)
        bin_string += (character_bin.rjust(8, "0") + " ")
        hex_string += (character_hex + " ")
        chr_string += character_chr
    print(bin_string)
    print(hex_string)
    print(chr_string)
    try:
        user_in = int(user_in)
    except:
        print("not an int")
        continue
    user_in = abs(user_in)
    print(round(user_in/3, 2))