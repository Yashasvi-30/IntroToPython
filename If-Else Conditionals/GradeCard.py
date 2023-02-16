#To print the grade card as per following conventions
# >90 - A
# >80 and <=90 - B
# >=60 and <=80 - C
# below 60 - D


print("*"*25)
print("\n Grade Card  \n")
print("*"*25)

name= input("Enter the Name of the Student  .")
roll= input("Enter the Roll No. of the Student .")
u= int(input("Enter the Percentage . "))

print("*"*25)

print("\n NAME : ",name)
print("\n Roll Number : ",roll)
print("\n Percentage : ",u)

if(u>90):
    print("\n Grade : A")

elif (u>80 and u<=90):
    
    print("\n Grade : B ")

elif (u>=60 and u<=80 ):
    
    print("\n Grade : C ")
else :
    print("\n Grade : D ")


print("*"*25)
