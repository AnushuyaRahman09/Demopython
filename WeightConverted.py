##Weight converted##
while True:
    print('''
    ------------------------------
    ''')
    weight = int(input("Weight: "))
    unit = input("(k)g or (L)bs: ")
    if unit == "k" or unit == "K":
        converted = weight / 0.45
        print("Weight in Lbs: ", converted)
        break
    elif unit == "l" or unit == "L":
        converted = weight * 0.45
        print("weight in Kgs: " + str(converted))
        break
    else:
        print("Invalid input")
        continue