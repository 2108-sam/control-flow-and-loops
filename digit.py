number=int(input("Enter your number: "))
print(f"\nYour number is {number}")
print(len(str(number)))
count=0
for digit in str(number):
    count+=1
print(f"Your {count}")