#Function Questions
# to sum all the numbers in a list


l=[1,2,3,4,5]
n=int (input("Enter the number of List Elements "))
l2=[]
for i in range (n):
    numbers = int(input('Enter number '))
    l2.append(numbers)
    
   
def sum(list1):
    total = 0
    for x in list1:
      
        total += x
    return total

print("The sum of sample list",sum(l))
print("The sum of user entered list",sum(l2))
