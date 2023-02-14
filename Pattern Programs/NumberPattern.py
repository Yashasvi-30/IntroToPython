#To Print a Number Pattern

#1
#12
#123
#1234
#12345

n = int(input("Enter the number of rows  you want. "))

#outer loop to handle number of rows

for i in range(0, n+1):
    
    # inner loop to handle number of columns  
    # values is changing according to outer loop
    
        for j in range(1, i + 1):  
            # printing stars  
            print(j, end = "" )
            #Bringing the cursor down
    
        print() 








