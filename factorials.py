n=int(input("Enter your number: "))
total=1
number=[]

for i in range(1,n+1):
    total *=i
    number.append(str(i))
print(" x".join(number) + f" = {total}")
print(f"Hence the factorials of {n} is {total}")