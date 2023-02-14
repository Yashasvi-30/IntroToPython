#To print the number pattern 5
#5 5 5 5 5 
#5 5 5 5 
#5 5 5 
#5 5 
#5 

n= int (input ("Enter the Number of rows you want. "))
m = int(input ("Enter the digit to print the pattern. "))

for i in range (1,n+1):
    for j in range (n,i-1, -1):
            print (m , end=" ")
    print ()
