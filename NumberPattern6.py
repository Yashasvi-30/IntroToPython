n=int(input("Enter the number of rows you want." ))

for i in range(1, n+1):
    num = 1
    for j in range(n, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print(num, end=' ')
            num += 1
    print("")            
