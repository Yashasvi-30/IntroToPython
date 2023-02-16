#Program to check if the number is divisible by another number or not.
print("*"*25)
print("\nDivisiblity Checker\n")
print("*"*25)

n=int(input("Enter a number to check divisiblity. \n"))
m=int(input("Enter a number whose divisiblity is to be checked . "))

if(m%n==0):
    print("The Number ",m," is divisible with the number ",n)

else:
    print("The Number ",m," is not divisible by the number ",n)


print("*"*25)
    
