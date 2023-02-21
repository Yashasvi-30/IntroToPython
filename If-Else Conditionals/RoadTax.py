#To print road tax according to the cost of bike


print("*"*25)
print("\n Road Tax Calculator \n")
print("*"*25)

name= input("Enter the Name   .")
roll= input("Enter the Phone Number .")
u= int(input("Enter the cost of the bike . "))

print("*"*25)

print("\n NAME : ",name)
print("\n Phone Number : ",roll)
print("\n Cost of Bike: ",u)

if(u>100000):
    print("\n Road Tax: ", (0.15*u))
          
if(u>50000 and u<=100000):
    print("\n Road Tax:  ", (0.10*u))

    
if(u<50000):
    print("\n Road Tax ", (0.05*u))

print("*"*25)
