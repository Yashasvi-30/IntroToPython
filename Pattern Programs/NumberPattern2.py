#To Print a Number Pattern2

#1 
#2 3 
#4 5 6 
#7 8 9 10 
#11 12 13 14 15 


n = int(input("Enter the number of rows  you want. "))

#outer loop to handle number of rows
a=0
for i in range(0, n+1):
    
    # inner loop to handle number of columns  
    # values is changing according to outer loop
    
        for j in range(1, i + 1):  
            # printing stars
            a=a+1
            print(a, end = "" )
            print(" " , end = "" )
            #Bringing the cursor down
    
        print() 
        
