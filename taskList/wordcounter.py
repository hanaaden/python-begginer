word = input("enter a word : ")

length = len(word)
print(length)


count = 0
s = {'a' , 'e' , 'i' , 'o' , 'u' , 'A' , 'E' , 'I' ,'O' , 'U'}
for c in word:
    if c in s:
        count = count + 1
print(f" the number of vowels are  {count}")

