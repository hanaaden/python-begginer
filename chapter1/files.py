import re 
fhand = open ( 'test.py', 'r')
for files in fhand:
    print(files)
print(fhand)


#counting lines 


count = 0
for line in fhand:
    count = count + 1
print(' the lines count are:  ' , count)

inp = fhand.read()
print(len (inp))
fhand.close()

#frequency of words

frequency = {}
file = open ('trying.py' , 'r')
read = file.read().lower()
finding = re.findall(r'\b[a-z]{3,15}\b',read)

for word in finding:
    count = frequency.get(word,0)
    frequency[word] = count +1 
    
frequency_list = frequency.keys()
for words in frequency_list:
     print( words , frequency[words])
    
file.close()

#writing a file
    
write_file = "I am learning the files in python now"

fb = open('write_demo.txt', 'w')
fb.write(write_file)
print('done writing')
fb.close()

fw= open('write_demo.txt', 'r')

for writes in fw:
    print(writes)
print(fw)
fw.close()

