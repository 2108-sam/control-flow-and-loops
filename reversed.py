number=input("Enter a number: ")
bew=""

for digit in number:
    bew = digit + bew
    new=number[::-1]

print(new)
print(bew)