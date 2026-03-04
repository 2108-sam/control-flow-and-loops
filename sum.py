n=int(input("Enter the range of number to calculate: "))
total=0
number=[]
for i in range(1,n+1):
    total +=i
    number.append(str(i))
print( " + ".join(number) + f" = {total}")