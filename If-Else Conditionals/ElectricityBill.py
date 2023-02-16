#To calculate the electricity Bill as per following conventions
# first 100 units - no charge
# next 100 units - rs. 5 per unit
# next 200 units - rs. 10 per unit

print("*"*25)
print("\n Electricity Bill \n")
print("*"*25)

name= input("Enter the Name of the User .")
phone= input("Enter the phone no. of the user.")
u= int(input("Enter the number of units consumed . "))

print("*"*25)

print("\n NAME : ",name)
print("\n Phone Number : ",phone)
print("\n Units Consumed : ",u)

if(u<=100):
    print("No Charge")

elif (u>100 and u<201):
    m=(u-100)*5
    print("Amount to be Paid: ",m)

else:
    i=(u-200)*10+(u-100)*5
    print("Amount to be Paid: ",i)


print("*"*25)
    
