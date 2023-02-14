#Program to print the number Pattern12
#5
#4 4
#3 3 3
#2 2 2 2
#1 1 1 1 1

n = int(input("Enter the number of rows you want. "))
m=n
for i in range(n): 
   for j in range(i+1): 
      print(m, end=' ')
   m=m-1   
   print()
