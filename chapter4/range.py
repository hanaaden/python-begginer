# Range with only a stop value
for i in range(5):
    print(i)
    
# Range with start and stop value
print("Range with start and stop value")
for i in range(2,5):
    print(i)

# Range with range(start,stop,step)
print("Range with a positive step size  ")
for i in range(0,10,2):
    print(i , end=" ")

#changing range into list
my_list = list(range(0, 3))
print(my_list)
