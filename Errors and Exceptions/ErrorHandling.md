# python Error Handling 

allows program handle unexpected events (like invalid input or missing files)
with out crashing 

python

n = 10
try:
    res = n / 0

except ZeroDivisionError:

    print("Can't be divided by zero!")

output will be Can't be divided by zero!

### Difference Between Errors and Exceptions
Errors and exceptions are both issues in a program, but they differ in severity and handling. Let's see how:

Error: Serious problems in the program logic that cannot be handled. Examples include syntax errors or memory errors.
Exception: Less severe problems that occur at runtime and can be managed using exception handling (e.g., invalid input, missing files).

Explanation: A syntax error stops the code from running at all, while an exception like ZeroDivisionError occurs during execution and can be caught with exception handling.

# syntax 

try:

      # Code 

except SomeException:

      # Code 
else:

     # Code 

finally:

    # Code 

try: Runs the risky code that might cause an error.
except: Catches and handles the error if one occurs.
else: Executes only if no exception occurs in try.
finally: Runs regardless of what happens useful for cleanup tasks like closing files.

try:

    n = 0
    res = 100 / n

except ZeroDivisionError:

    print("You can't divide by zero!")

except ValueError:

    print("Enter a valid number!")

else:

    print("Result is", res)

finally:

    print("Execution complete.")


try block attempts division, except blocks catch specific errors, else block executes only if no errors occur, while finally block always runs, signaling end of execution.

Advantages
Below are some benefits of using exception handling:

### Improved reliability: 
Programs don’t crash on unexpected input.
### Separation of concerns: 
Error-handling code stays separate from business logic.
### Cleaner code: 
Fewer conditional checks scattered in code.
### Helpful debugging: 
Tracebacks show exactly where the problem occurred.

## Disadvantages
Exception handling have some cons as well which are listed below:

### Performance overhead: 
Handling exceptions is slower than simple condition checks.
### Added complexity: 
Multiple exception types may complicate code.
### Security risks: 
Poorly handled exceptions might leak sensitive details.

The try statement works as follows.

First, the try clause (the statement(s) between the try and except keywords) is executed.
If no exception occurs, the except clause is skipped and execution of the try statement is finished.
If an exception occurs during execution of the try clause, the rest of the clause is skipped. Then, if its type matches the exception named after the except keyword, the except clause is executed, and then execution continues after the try/except block.
If an exception occurs which does not match the exception named in the except clause, it is passed on to outer try statements; if no handler is found, it is an unhandled exception and execution stops with an error message






