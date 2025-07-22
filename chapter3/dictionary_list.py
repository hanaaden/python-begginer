#collectio we put more than one value in it and carry them all around one pacakege 
    #what is not collection
#most our variable are one value 

#Story of two collections
# - list is a linear collection of values look up by position 0 .. lenght -1
# - dictionary is a linear collection of key value pairs lookup "tags" or "key"

#dictionary is most powerfull data collection in python

# abstract object =  lists dictionary and tuples

#list
cards = list()
cards.append(12)
cards.append(7)
cards.append(3)
print(cards)
cards[2] = cards[2] + 2
print(cards)

#dictionary

seasons = dict()
seasons['summer'] = 12
seasons['fall'] = 3
seasons['spring'] = 7

print(seasons)
print (seasons['fall'])
seasons['fall'] = seasons['fall']+2
print(seasons)

#dictionary literal = use curly braces and have key : value 

students = {'chuck': 1 , 'fred': 24 , 'jan': 30}
print(students)
counts = dict()
names = {'john' ,' jie' ,'milson' ,'fred'}

for name in students:
    if name not in names:
        print('not found')
    else:
        print('found')

#sliced

t = [9,41,34,45,12,7]
t[1:3]
print(t[1:3])
print(t[3:])
print(t[:4])