words = ["cat" , "dog" , "windows" , "car"]
for r in words:
    print(r , len(r))
    
users = {"Hans" : "active" , "Eleonore" : "inactive" , "John": "active"}

#strategy : create a new collection
print("=== strategy : create a new collection === ")
active_users = {}
for user,status in users.items():
    if status == "active":
        active_users[user] = status
print(active_users)
#

    
    
