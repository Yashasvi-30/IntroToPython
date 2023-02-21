#Accept the following from the user
#and calculate the percentage of class attended:

#Total number of working days
#Total number of days for absent
#After calculating percentage show that, If the percentage is less than 75,
#than student will not be able to sit in exam.
print("**** Attendance Calculator ****")

nd = int (input("Enter total number of working days"))
na = int(input("Enter number of days absent"))
per=(nd-na)/nd*100
print ("Your attendance is ", per)
if per <75 :
 print ("\nYou are not eligible for exams")
else:
 print ("\nYou are eligible for writing exam")
