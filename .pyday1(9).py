T=int(input("enter the value of T: "))
E=[3,5,2,0]
L=[0,2,4,4]
x=[0,0,0,0]
for i in range(0,T):
    x[i]=(x[i-1]+E[i])-L[i]
    print(x[i])
print("max guests:",max(x))
