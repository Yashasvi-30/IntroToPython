#This is a Python Program to check if two numbers are amicable numbers.
#Check if the sum of the proper divisors is equal to the opposite numbers.
#If they are equal, they are amicable numbers.

x=int(input('Enter number 1: '))
y=int(input('Enter number 2: '))
sum1=0
sum2=0
for i in range(1,x):
    if x%i==0:
        sum1+=i
for j in range(1,y):
    if y%j==0:
        sum2+=j
if(sum1==y and sum2==x):
    print('Amicable!')
else:
    print('Not Amicable!')
