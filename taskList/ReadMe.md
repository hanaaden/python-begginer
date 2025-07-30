## 1: Explain how Python's interpreted nature benefits rapid application development.

strengths to accelerate software development, emphasizing speed, flexibility, and user involvement.
Key aspects of RAD in Python:
Simplicity and Readability:
Python's concise and readable syntax allows developers to write less code, reducing development time and improving collaboration.
Rich Ecosystem:
Python boasts a vast collection of libraries and frameworks, such as Django 

Agile Alignment:
Python's flexibility and ease of iteration align well with agile development principles,
Cross-Platform Compatibility:
Python applications can be developed to run on various operating systems


## 2: Python supports high-level data types like lists and dictionaries. Why are these considered more flexible than data structures in low-level languages like C?

1. Dynamic Sizing:
Python:
Lists and dictionaries are dynamically sized.

C:
Arrays in C have a fixed size determined at compile time. 

Python:
Lists and dictionaries can store elements of different data types within the same collection. 

C:
C arrays are typically homogeneous, meaning they can only store elements of a single, specified data type.


## 3: Research and write a Python script that prints the current date and time using a built-in module 
we first use a module that we import - import datetime
the code is in te date.py

## 4: Imagine you are renaming thousands of photo files. Write pseudocode for how Python could help automate this.

By leveraging the os.rename() function within a loop, you can systematically rename a large number of files based on various criteria, such as sequential numbering or incorporating metadata from the image file

## 5: What is the difference between running a script using python script.py and running Python in interactive mode?

### In script 
a python program can be written in a file. This file can then be saved and executed using the command prompt.
Script mode is very suitable for writing long pieces of code.

### Interactive mode 
is based on this ideology only. In the interactive mode as we enter a command and press enter, the very next step we get the output.
Means we use the command line
## 6: Write a script that prints the name of the script and any command-line arguments passed to it. 

## 7: Try running a Python one-liner using python -c to print numbers from 1 to 5 using a loop.

## 8: How does Python handle type conversion between integers and floating point numbers in expressions?
float(): Converts an integer or a number-like string to a float.
int(): Converts a float or a number-like string to an integer. When converting a float to an integer, the decimal part is truncated (removed), not rounded.

## 9: What is the significance of the underscore variable _ in interactive mode?
it automatically stores the result of the last evaluated expression.

## 10: Write a program that takes a user input string and counts how many vowels it contains.
   you will find the code in counter.py

## 11: Create a list of numbers, then, square each number, keep only the ones greater than 50, print the result.
   you will find the code in lister.py

## 12: What is the purpose of the else clause in a loop, and how does it behave differently from the if statement’s else?
else in loops is used to be executed at the end means when the condition of the loop becomes false 

The else block just after for/while is executed only when the loop is NOT terminated by a break statement.
`l = [9,8,7]`
`n = len(l)`
`i = 0`
`while i < n:`
   ` if l[i] % 2 == 0:`
        `print("we found even")`
        `break`
   ` i += 1`
`else:`
   ` print("we did not find even ")`

## 13: Describe a scenario where continue would be more useful than break in a loop.
When the continue statement is executed, the loop doesn't terminate but skips to the next iteration.
This is useful when you want to skip over certain conditions but keep the loop running.

## 14: Simulate a simple login system: Give the user 3 chances to enter the correct password, use a while loop and break to stop early if the password is correct, print “Access Denied” if all attempts are used.
 you will find the code in password.py

## 15: What happens to sys.argv when you run a script using the -c and -m options?

