##Function Questions
# to find all prime  numbers in a list


l=[1,2,3,4,5]
n=int (input("Enter the number of List Elements "))
l2=[]
for i in range (n):
    numbers = int(input('Enter number '))
    l2.append(numbers)
    
   
def prime (list1):
    
    for x in list1:
        count=0
        for i in range(1,x+1):
            if(x%i==0):
                count=count+1
            
        if(count==2):
          print (x," is a prime number")    
    print()    

prime(l)
prime(l2)
