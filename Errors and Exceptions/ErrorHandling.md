# python Error Handling 

allows program handle unexpected events (like invalid input or missing files)
with out crashing 

python
,,,
n = 10
try:
    res = n / 0
except ZeroDivisionError:
    print("Can't be divided by zero!")
',,,

output will be Can't be divided by zero!

### Difference Between Errors and Exceptions
Errors and exceptions are both issues in a program, but they differ in severity and handling. Let's see how:

Error: Serious problems in the program logic that cannot be handled. Examples include syntax errors or memory errors.
Exception: Less severe problems that occur at runtime and can be managed using exception handling (e.g., invalid input, missing files).
