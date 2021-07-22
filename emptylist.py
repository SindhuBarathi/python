a=int(input("enter a number"))
b=int(input("enter a number"))
large=[]
small=[]
def compareMe(a,b):
    if a>b:
        large.append(a)
        small.append(b)
    else:
        small.append(a)
        large.append(b)
compareMe(a,b)
print(large)
print(small)