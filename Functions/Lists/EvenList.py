#Function Questions
# to find all even  numbers in a list


l=[1,2,3,4,5]
n=int (input("Enter the number of List Elements "))
l2=[]
for i in range (n):
    numbers = int(input('Enter number '))
    l2.append(numbers)
    
   
def even (list1):
    
    for x in list1:
        
        if(x%2==0):
          print (x," is an even  number")    
    print()    

even(l)
even(l2)
