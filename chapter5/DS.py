from collections import deque
# friuts = ["apple" , "orange" , "pineapple" , "banana","apple"]
# print(friuts.count("apple"))
# # 2
# print(friuts.index("banana"))
# #3
# friuts.append("grape")
# friuts.reverse()
# print(friuts)
# friuts.sort()
# print(friuts)
# friuts.pop()
# print(friuts)

# squares = []
# for x in range(10):
#     squares.append(x++2)
#     print(squares)
    
    
#exercises
arr = []
for i in range(5):
    arr.append(i)
print(arr)
print("before removing")
for j in range(5):
    arr.pop()
    print(arr)
    
    
    
queu = deque(["alice" , "pop" , "pop"])
queu.append("dailo")
print(queu)
queu.popleft()
print(queu)
#list comprehention

lis = [ x*x for x in range(10)]
print(lis)

# nested list comprehension

matrix = [[1,2,3] , [4,5,6] ]
flat = [num for row in matrix  for num in row]
print(flat)

#del statement 
a = [1,2,3,4,5]
del a[1]
print(a)

#tuples : list you cannot change
t = (1,2,3)
print(t[0])

# nested tuple 
d = ((1,2,3) , (4,5,6))
print(d)

#SET
f = {1,2,2,3}
print(f)

#disctionary 
capital = {"france": "paris" , "italy" : "rome"}
print(capital)

letter = ["a" , "b" ,"c"]
for i , val in enumerate(letter):
    print(i,val)
    
country = ["italy" , "india" , "US"]
for i , cal in enumerate(country):
   print(i , cal)
print([1,2,3] < [1,2,4])