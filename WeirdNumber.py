##weird##
n=int(input("enter a number:"))
if n%2==1 :
    print("weird")
elif n%2==0 and n in range (2,6):
    print("not weird")
elif n%2==0 and n in range (6,20):
    print("weird")
elif n>0 and n%2==0 :
    print("not weird")
else:
    pass