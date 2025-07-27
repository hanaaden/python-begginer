lis = [2,4,5,9]
newlis = []
print(lis)
i = 0
for t in lis:
     v = lis[i]
     d = v * v
     if d > 50:
        newlis.append(lis[i]) 
     i = i+ 1
     
print(f'the square of {newlis} is greater than 50')