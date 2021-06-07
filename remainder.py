n=int(input())#1234
#i=0
#count=0
#while n!=0:
    # r=n%10
   #  n=n//10
   #  count=count+1
#print(count)
n=int(input())
e=0
o=0
c=0
while n:
    c=c+1
    n=n//10
    if c%2==0:
       e+=1
    else:
        o+=1
if e%2==0 and o%2!==0:
    print('even odd')
elif e%2==0 and o%2==0:
     print("even")
elif e%2!==0 and o%2!==0:
      print("odd")
else:
      print('mixed')
     

