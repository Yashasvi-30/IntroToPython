#Program to display if a person is eligible to vote or not
#also Calculate the years left in becoming eligible

print("*"*25)
print("Voting Eligibility Checker")

print("*"*25)
n=int(input("Enter the legal age of the candidate : "))

print("The voting criteria states that in order to cast a vote an individual should be of or above 18yrs of age")

if(n>=18):
    print("\nHoorayy!!! You are Eligible to vote. ")
    print("*"*25)


else:
    print("\nOops ! You are not eligible to vote right now. ")
    m=18-n
    print("You still  have ",m," years left to vote.")
    print("*"*25)


    
