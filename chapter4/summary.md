# more about controls
pythons for statement iterates over the items of any sequence in **forstatement.py**

# the range() function find the code range.py
Python’s range acts as a built-in function, and is commonly used for looping a specific number of times in for-loops. 
### There are three ways to call the range function:

### With one integer argument it
### counts from 0 to stop
range(stop)
`for i in range(5):`
   `print(i)`
 range stops as soon as it reaches the stop value, and won’t return the stop value itself. why Computers start counting at zero, while humans start counting at 1
### With two integer arguments it
### counts from start to stop
range(start, stop)
A call to range(2, 5) will return the values 2, 3, and 4. Here’s another example
`for i in range(2,5)`
`  print(i)`
### With three integer arguments it
### counts from start to stop,
### with a defined step size
range(start, stop, step)
range() takes an optional argument that’s called the step size. The step size defines how big each step is between the calculated numbers

if you need a iteration of sequence number the build in function 
range() comes in handy 
for varibale in range(number)

In many ways the object returned by range() behaves as if it is a list, but in fact it isn’t. It is an object which returns the successive items of the desired sequence when you iterate over it, but it doesn’t really make the list, thus saving space.

# break and continue in break_con.py
### break Statement
Purpose: Immediately exits the loop, regardless of the loop's condition.
Use Case: When you want to stop the loop as soon as a specific condition is met. 

### continue Statement
Purpose: Skips the current iteration and moves to the next one.
Use Case: When you want to skip certain iterations based on a condition.

# else clause on loops
if the loop finishes wothout executing the break the else clouse executes
- in for loop the else clause is executed after the loop finishes its iteration
that is if no break occurred 
- in while loop its executed after the loop's condition becomes false 
- the else clause is not executed if the loop was terminated by break

## the pass statement
The pass statement in Python is a placeholder that does nothing when executed
Purpose: It allows you to write code that is syntactically correct but does nothing during execution.
se Cases:
Empty Functions or Classes: When you want to define a function or class but haven't implemented it yet.
Conditional Statements: To handle cases where no action is required for a specific condition.
Loops: To create loops that do nothing temporarily.
for ex: `while True:`
           `pass`
           or
        `class MyBox:`
           `pass`

# match statement in match.py
match statement takes expression and compares its value to successsive patterns given one or more CASE BLOCK
It allows you to write cleaner and more readable code compared to multiple if-elif-else statements

# Defining Functions in functions.py
functions are blocks of reusable code that perform a specific task. They are defined using the def keyword. Here's a concise guide to defining and using functions:
def function_name(parameters):
    """
    Optional docstring: Describes the function.
    """
    # Function body
    return value  # Optional
## Types of Arguments in Python
### 1: Positional Arguments:
Passed in the same order as the parameters.
### 2. Keyword Arguments:
Specify the parameter name explicitly.
print(add(b=5, a=3))  # Output: 8
### 3. Default Arguments:
parameters with default values.
### 4>  arbitrary argument
Parameters with default values.
Allow passing a variable number of arguments.





