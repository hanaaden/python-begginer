file = open("file.txt" , "w")
file.write("Hard work is one of the most valuable qualities a person can have. It is the key to achieving goals and turning dreams into reality. While talent can help, it is hard work that truly makes the difference between success and failure. Every great achievement in history has come from people who were willing to put in time, effort, and dedication.")
file.close()

File = open("file.txt" , "r")
content = File.read()
print(content)
File.close()

with open("file.txt" , "r") as file:
    content = file.read()
words = content.split()
word_count = len(words)
print("words in file" , words)
print("Total number of words " , word_count)

      

