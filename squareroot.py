b=int(input("enter a number:"))
c=int(input("enter a number"))
d=int(input("enter a number"))
list1=[b,c,d]
def sqr(a):
    return a**2
print(list(map(sqr,list1)))