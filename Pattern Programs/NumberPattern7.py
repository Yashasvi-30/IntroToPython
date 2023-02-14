#Program To print Number Pattern 7
#5 4 3 2 1
#5 4 3 2
#5 4 3
#5 4
#5

n =int(input("Enter the number of rows you want." ))

for i in range (0,n+1):
    for j in range (n,i,-1):
        print(j,end=" ")
    print()
             
             
