#Write a program to accept percentage and
#display the Category according to the following criteria:

#Percentage - Category
#< 40         failed
#>=40 & <55 fair

#>=55 & <65 good
#>=65       excellent

pr = int (input ("Enter the percentage"))
if pr < 40:
    print("Your Category is: Failed")
elif pr >= 40 and pr < 55:
    print ("Your Category is: Fair")
elif pr >=55 and pr < 65:
    print ("Your Category is: Good")
elif pr >= 65 and pr<=100:
    print ("Your Category is: Excellent")
elif pr >100:
    print ("Please enter correct percentage")
