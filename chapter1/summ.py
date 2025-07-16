x=9
try:
  s=x/0
  print(s)
except :
  print("the try is not working")

sti="you"
try:
  y=int(sti)
except :
  print("sti cant be integer")


L=[2,4,7,8]
print(L)
#add element 
L.append(10)
print(L)
#insert 
L.insert(0,15)
print(L)
print(L[3])
#update
L[3]=23
print(L)
print(L[3])

#for loop
print("the for loop")
for i in L:
  print(i)

#while loop
print("the while loop")
i=0
while i<10:
  print(i)
  i=i+1

#tuple 
print("the tuple")
t=(1,2,3)
print(t)
print(t[1])

#sets
print("creation of set")
s={2,3}
print(s)
#update
s.update([4,5])
print(s)
#add
s.add(7)
print(s)

#dictionary
dic={1:'a', 2:'b'}
print(dic)
print(dic.keys())
print(dic.items())



for i in range(10):
  if(i%2==0):
    print("even")
  else:
    print("odd")
 

