i = 0
while i<10:
    print(i)
    i += 1
else:
    print("over")
    
l = [9,8,7]
n = len(l)
i = 0
while i < n:
    if l[i] % 2 == 0:
        print("we found even")
        break
    i += 1
else:
    print("we did not find even ")