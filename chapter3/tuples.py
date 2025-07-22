#tuple is sequence of value much like a list
#values that is stored in tuple can be any type and irs indexed

t = ('a',)
print(type(t))
t1 = ('a')
print(type(t1))

y = ('w', 'h', 'a', 't')
print(y[0])
print(y[1:3])

#comparism
if (10, 12, 0) > (3, 4, 0):
    print('true')
else:
    print('false')
    
#assigment tuple

w = ('Hello', 'winner')
x , r = w
print(x)
print(r)