# indefinite loop 

n = 5
while n > 0:
    print (n)
    n = n-1
print ('bro')

while n > 0:
    print ('real')
print ("bob")

#break and continue 

while True:
    line = input ('>')
    if line [0] == '#':
        continue
    if line == 'Done':
        break
    print (line)
    
print ('Done')

# definite loop

for i in [5, 4, 3, 2, 1]:   # i is iteration variable [5,4,3,2,1] is sequence print is body block
    print (i)
print ('off')

#finding the average
zork = 0
sum = 0
for i in [5, 4, 3, 2, 1]:
    print(i)
    zork= zork + 1
    sum = sum + i
print (' the average of this is: ' , sum / zork )

    
friends = ['john' , 'joshef', 'jeo']
for friend in friends:
    print ('happy birthday', friend)
print ('Done')