#Program to print number pattern8
#5 4 3 2 1
#4 3 2 1
#3 2 1
#2 1
#1

n=int (input ("Enter the number of rows you want. "))
p=n
for i in range (0,n+1):
    p=n
    p=p-i
    for j in range (n,i,-1):
       print(p,end=" ")
       p=p-1
    
    print()   
