#To Print a Star Pattern
n = int(input("Enter the number of rows  you want. "))

#outer loop to handle number of rows

for i in range(0, n):
    
    # inner loop to handle number of columns  
    # values is changing according to outer loop
    
        for j in range(0, i + 1):  
            # printing stars  
            print("*", end = "" )
            #Bringing the cursor down
    
        print()        
        
