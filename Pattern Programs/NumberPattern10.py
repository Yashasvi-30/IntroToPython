#program to NumberPattern10
#  0
#  2 2
#  4 4 4
#  6 6 6 6
#  8 8 8 8 8


n=int(input("Enter the number of rows you want."))
p=0
for i in range (n):
    for j in range (i+1):
        print (p, end = ' ')
    p+=2
    print()

