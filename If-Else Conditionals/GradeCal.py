#Accept the percentage from the user and display the grade according to the following criteria:

#Below 25-- D
#25 to 45 -- C
#45 to 50 -- B
#50 to 60 -- B+
#60 to 80 - A
#Above 80 -- A+

print("Grade Calculator")
per = int (input ("Enter percentage"))
if per> 80:
    print("\nGrade is A+")
elif per >60 and per <=80:
    print("\nGrade is A")
elif per > 50 and per <=60:
    print("\nGrade is B+")
elif per > 45 and per <=50:
    print("\nGrade is B")
elif per > 25 and per <=45:
    print("\nGrade is C")
elif per <25:
    print("Grade is D")
