#Program to print the NumberPattern9
#        0
#      1 2
#    3 4 5
#  6 7 8 9

n= int(input("Enter the number of rows you want."))
count = 0;

for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" " ,end="")
    for j in range(1,i+1):
        print (count ,end="")
        
        count=count+1
    print()

    
 
