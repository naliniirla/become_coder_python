n,r1,r2=map(int,(input().split())
if r1<=r2:
    r1,r2=r2,r1
while r1>=r2:
     print(n,'X',r1,'=',n*r1)
     r1-=1
