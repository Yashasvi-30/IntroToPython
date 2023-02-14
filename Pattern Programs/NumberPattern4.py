#To Print a Number Pattern4
#11111
#2222
#333
#44
#5


n = int(input("Enter the number of rows  you want. "))

#outer loop to handle number of rows

for i in range(1, n+1):
    
    # inner loop to handle number of columns  
    # values is changing according to outer loop
    
        for j in range(n,i-1,-1):  
            # printing stars  
            print(i, end = "" )
            #Bringing the cursor down
    
        print() 
