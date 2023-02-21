#Accept the age of 4 people and display the oldest one.
age1=int(input ("Enter age of first person"))
age2=int(input ("Enter age of second person"))
age3=int (input ("Enter age of third person"))
age4=int(input("Enter age of fourth person"))

if age1 > age2 and age1 > age3 and age1 > age4:
 print ("Age of oldest person is ",age1)
if age2 > age1 and age2 > age3 and age2 > age4:
 print("Age of oldest person is ",age2)
if age3 > age2 and age3 > age1 and age3 > age4:
 print ("Age of oldest person is ",age3)
if age4 > age1 and age4 > age2 and age4 > age3:
 print ("Age of oldest person is ",age4)

print("*"*25)

age1=int(input ("Enter age of first person"))
age2=int (input ("Enter age of second person"))
age3=int (input("Enter age of third person"))
age4=int(input("Enter age of fourth person"))
if age1 < age2 and age1 < age3 and age1 < age4:
    print ("Age of oldest person is ", age1)
if age2 < age1 and age2 < age3 and age2 < age4:
    print ("Age of oldest person is ",age2)
if age3 < age2 and age3 < age1 and age3 < age4:
    print ("Age of oldest person is ",age3)
if age4 < age1 and age4 < age2 and age4 < age3:
    print("Age of oldest person is ", age4)

print("*"*25)    
