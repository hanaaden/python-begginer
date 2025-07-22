words = ["cat" , "dog" , "windows" , "car"]
for r in words:
    print(r , len(r))
    
users = {"Hans" : "active" , "Eleonore" : "inactive" , "John": "active"}

#strategy : create a new collection
active_users = {}
for user,status in users.items():
    if status == "active":
        active_users[user] = status
print(active_users)

#the range() function
for i in range(10):
    print(i)
    
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
print(users)
    
l = ["mary" , "spong" , "eifh" , "jony"]
for i in range(len(l)):
    print(i , l[i] )
    
#break and continue statement
for n in range(2,10):
    for r in range(2,n):
        if n%r==0:
         print(f"{n} equals {r} * {n//r}"  , r)
         break
     
#continue 
for a in range(2,10):
    if a%2==0:
        print("found even number:", a)
    else:
        print("found odd number:" , a)
        
#else Clauses on Loops