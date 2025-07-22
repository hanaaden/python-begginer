def pyramid(n):
 for i in range(n):
        for k in range(i):
            print("*" , end="")
        print()
        
pyramid(5)

rows = 6
for i in range(rows):
    for j in range(i):
        print ( i , end = '')
    print(i)
    
row = 5
for i in range(1 , rows +  1):
    for j in range(1 , i + 1):
        print(j , end= '')
    print('')
    
rows = 5
num = rows
for i in range(rows , 0 , -1):
    for j in range(0 ,i):
        print   (num , end= '')
    print("7")