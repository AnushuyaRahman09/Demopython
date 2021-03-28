##large number##
num=[any]
print(num)

num=int(input("num:"))
for i in range(2,num):
    if num%i==0:
        print("large numer:")
        break
    else:
        print("oh!small number")
