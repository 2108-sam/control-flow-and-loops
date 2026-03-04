num=int(input("Enter the number to be multiplied: "))
for x in range(0,21):
    prod=num*x
    print(f"{num} X {x} = {prod}")

num = int(input("Enter the number to be multiplied: "))

table = [f"{num} x {x} = {num*x}" for x in range(1, 11)]  # Create all multiples
print(", ".join(table))  # Join them with commas