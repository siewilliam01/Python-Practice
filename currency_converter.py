
def to_IDR(USD):
    IDR = USD * 16335.571
    IDR = round(IDR, 0)
    return IDR

def to_CAD(USD):
    CAD = USD * 1.4317
    CAD = round(CAD, 2)
    return CAD

def to_GBP(USD):
    GBP = USD * 0.8063
    GBP = round(GBP, 2)
    return GBP

def main():
    convert_to = input("Convert USD to >>> ")
    USD_in = input("Enter USD dollar value >>> ")
    try:
        USD_in = int(USD_in)
    except:
        print(USD_in, "is not a valid quantity, try again.")
    else:
        if(convert_to == "IDR"):
            print(to_IDR(USD_in))
        elif(convert_to == "CAD"):
            print(to_CAD(USD_in))
        elif(convert_to == "GBP"):
            print(to_GBP(USD_in))
        else:
            print("Not a compatible currency")

print("Compatible with IDR, CAD, GBP")
while True:
    main()