##Function Questions
# to find factorial of  all the numbers in a list


l=[1,2,3,4,5]
n=int (input("Enter the number of List Elements "))
l2=[]
for i in range (n):
    numbers = int(input('Enter number '))
    l2.append(numbers)
    
   
def factorial(list1):
    
    for x in list1:
        total=1
        for i in range(1,x+1):
            total *= i
        print("Factorial of ",x," is : ", total)
    print()    

factorial(l)
factorial(l2)
