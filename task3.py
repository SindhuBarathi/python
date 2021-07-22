n=int(input("enter a number:"))
even=[]
odd=[]
def evenOdd(n):
    if(n%2==0):
        even.append(n)
    else:
        odd.append(n)
evenOdd(n)
print(even)
print(odd)

