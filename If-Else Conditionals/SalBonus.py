#A company decided to give bonus to employee according to following criteria:
#Time period of Service Bonus
#More than 10 years 10%
#>=6 and <=10 8%
#Less than 6 years 5%
#Ask user for their salary and years of service and print the net bonus amount.

ser=int (input ("Enter the time period of service"))
sal =int (input("Enter your salary"))
if ser > 10:
    b=10/100*sal
if ser >=6 and ser <=10:
    b = 8/100*sal
if ser < 6:
    b = 5/100*sal
print ("Bonus is ", b)
