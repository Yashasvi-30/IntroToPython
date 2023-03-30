#Function Questions
# to find  sum of all odd and even  numbers in a list


l=[1,2,3,4,5]
n=int (input("Enter the number of List Elements "))
l2=[]
for i in range (n):
    numbers = int(input('Enter number '))
    l2.append(numbers)
    
   
def eveodd(list1):
    sumeve=0
    sumodd=0
    for x in list1:
        
        if(x%2!=0):
            sumodd+=x
        else:
            sumeve+=x
    print("\tSum of Even elements : \t", sumeve)
    print("\n\tSum of Odd elements : \t",sumodd)

eveodd(l)
eveodd(l2)
