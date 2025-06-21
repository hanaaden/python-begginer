#handle = open ( filename, mode) 
# reading file
fhand = open ( 'test.py', 'r')
for cheese in fhand:
    print(cheese)
print (fhand)

#counting lines 
import re 
fright = open('test.py' , 'r')
count = 0
for line in fright:
    count = count + 1
print(' the lines count are:  ' , count)

inp = fhand.read()
print (len (inp))

frequency = {}
file = open ('test.py' , 'r')
read = file.read().lower()
finding = re.findall(r'\b[a-z]{3,15}\b',read)

for word in finding:
    count = frequency.get(word,0)
    frequency[word] = count +1 
    
frequency_list = frequency.keys()
for words in frequency_list:
     print ( words , frequency[words])
    
