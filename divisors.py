num=int(input("enter number:"))
print("the divisors of the number are:")
for i in range(1,num+1):
    if(num%i==0):
        print(i)