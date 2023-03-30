#Function Questions
# to multiply all the numbers in a list


l=[1,2,3,4,5]
n=int (input("Enter the number of List Elements "))
l2=[]
for i in range (n):
    numbers = int(input('Enter number '))
    l2.append(numbers)
    
   
def multiply(list1):
    total = 1
    for x in list1:
      
        total *= x
    return total

print("The product of sample list",multiply(l))
print("The product of user entered list",multiply(l2))
