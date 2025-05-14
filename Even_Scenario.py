W=int(input("Enter the weight of the watermelon: "))
if(W%2!=0):
    print("NO")
else:
    x=W//2
    if(x%2==0):
        print(x,x)
    else:
        print(x-1,x+1)

print("==============================")

x=int(input())
if x<5:
    print(1)
elif x%5==0:
    print(x//5)
else:
    print((x//5)+1)

print("==============================")

n,m=map(int,input().split())
if(n%m==0):
    print(n//m)
else:
    print((n//m)+(n%m))
