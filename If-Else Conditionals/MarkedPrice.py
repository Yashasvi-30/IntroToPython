#Accept the marked price from the user and
#calculate the Net amount as(Marked Price -
#Discount) to pay according to following criteria:
#Marked Price Discount
# >10000 20%
# >7000 and <==10000 15%
# <=7000 10 %


na=0
d=0
mp=int (input ("Enter marked price: "))
if mp > 10000:
 d = 20/100*mp
if mp > 7000 and mp <= 10000:
 d= 15/100*mp
if mp <= 7000:
 d= 10/100*mp
na = mp-d
print ("Net amount to pay : ", na)
