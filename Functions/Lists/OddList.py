#Function Questions
# to find all odd  numbers in a list


l=[1,2,3,4,5]
n=int (input("Enter the number of List Elements "))
l2=[]
for i in range (n):
    numbers = int(input('Enter number '))
    l2.append(numbers)
    
   
def odd(list1):
    
    for x in list1:
        
        if(x%2!=0):
          print (x," is an odd  number")    
    print()    

odd(l)
odd(l2)
