#Function Questions

#To print the maximum of three of digits

n=int(input("Enter a digit."))
m=int(input("Enter a digit."))
o=int(input("Enter a digit."))

def maxtwo(a,b):
    if(a>b):
        return a
    else:
        return b

def maxthree(x,y,z):
    j= maxtwo(x,y)
    k= maxtwo(z,j)

    return k



print("The Maximum Number is :",maxthree(n,m,o))
    
