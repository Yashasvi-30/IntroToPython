#Program to check if last digit of number is divisible by 3 or not

n=(int(input("Enter the Number : ")))

if((n%10)%3==0):
    print("The Last Digit ", (n%10)," of the number entered ",n," is divisible by 3")
else:
    print("The Last Digit ", (n%10)," of the number entered ",n," is not divisible by 3")
    
    
