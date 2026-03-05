first=0
second=1
n=int(input("Enter The nth number: "))
total=0
if n <0:
    print("Number should be greater than or equals to 0")
elif n==1:
    print(f"{first}")
else:
    print(first, second, end=",")
    for  i in range(1,n+1):
        next=first+second
        print(next, end=" ,")
        first=second
        second=next