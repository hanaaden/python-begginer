#break and continue statement
print("=== break and continue statement ===")
for n in range(2,10):
    for r in range(2,n):
        if n%r==0:
         print(f"{n} equals {r} * {n//r}"  , r)
         break
     
#continue 
print("=== continue ===")
for a in range(2,10):
    if a%2==0:
        print("found even number:", a)
    else:
        print("found odd number:" , a)
        
#else Clauses on Loops
print("=== else Clauses on Loops ===")
for n in range(1,10):
    if n%2==0:
        print("the even number is: " , n)
        break
    else:
        print("this is odd")