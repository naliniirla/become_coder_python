n=int(input())
e=0
o=0
while n:
    r=n%10
    n=n//10
    if(r%2==0):
        e+=1
    else:
        o+=1
print(e)
print(o)
