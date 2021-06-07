n=5
res=0
while True:
    r=n%10
    n=n//10
    res=res*10+r
    print(r,end=" ")
