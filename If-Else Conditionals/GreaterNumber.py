#Program to find the greater of the two numbers

print("*"* 25)
print("\nGreater Number Checker\n")
print("*"* 25)

n=(int(input("Enter the first number. ")))
m=(int(input("Enter the second number. ")))


if (n>m):
    print(n," is greater than ",m)
    print("*"* 25)

else:
    print(m," is greater than " , n)
    print("*"* 25)
