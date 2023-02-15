#This Program is to build a Basic Calculator
print ("Calculator")
print("*"*15)
n=1
while (n>0):
    print("/n Enter 1 for Addition")
    print("/n Enter 2 for Subtraction")
    print("/n Enter 3 for Multiplication")
    print("/n Enter 4 for Division")
    print("/n Enter 5 for Raising Power")
    print("/n Enter 6 for Finding Remainder")
    print("/n Enter 7 for Floor Division")
    print("/n Enter 8 for Terminating the Process")
    print("*"*15)

    c=int(input("Enter Your Choice . "))
    print("*"*15)

    if c==1:
        #This is a program to add two numbers
        n=int(input("Enter First Number"))
        m=int(input("Enter Second Number "))

        o=n+m

        print(n,"+",m,"=",o)

    elif c==2:
    
        #This is a program to subtract two numbers
        n=int(input("Enter First Number"))
        m=int(input("Enter Second Number "))

        if n>m :
            o=n-m
            print(n,"-",m,"=",o)

        else:
            o=m-n
            print(m,"-",n,"=",o)

    elif c==3:
        #This is a program to multiply two numbers
        n=int(input("Enter First Number"))
        m=int(input("Enter Second Number "))

        o=n*m

        print(n,"*",m,"=",o)

    elif c==4:
        #This is a program to divide two numbers
        n=int(input("Enter First Number"))
        m=int(input("Enter Second Number "))

        o=n/m

        print(n,"/",m,"=",o)


    elif c==5:
        #This is a program to find exponent
        n=int(input("Enter the Base Number"))
        m=int(input("Enter the Power"))

        o=n**m

        print(n,"^",m,"=",o)

    elif c==6:
        #This is a program to find remainder
        n=int(input("Enter First Number"))
        m=int(input("Enter Second Number "))

        o=n%m

        print(n,"%",m,"=",o)

    elif c==7:

        #This is a program to find quotient to whole number (floor division)
        n=int(input("Enter First Number"))
        m=int(input("Enter Second Number "))

        o=n//m

        print(n,"//",m,"=",o)
    
    
    else:
        n=0

print("*"*15)        
    

    
    
    
    
    
