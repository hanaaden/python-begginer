2.1 Invoking the Interpreter
The Python interpreter is usually installed as /usr/local/bin/python3.13 on systems where it is available. By including /usr/local/bin in your Unix shell’s search path, you can start the interpreter using:

bash
Copy
Edit
python3.13
Since the installation path can vary, check with your system administrator if it's located elsewhere (e.g., /usr/local/python).

On Windows
If Python is installed from the Microsoft Store, the python3.13 command is available.

If the py.exe launcher is installed, you can use:

bash
Copy
Edit
py
Refer to Excursus: Setting environment variables for additional launch methods.

Exiting the Interpreter
Unix: Press Control-D

Windows: Press Control-Z, then Enter

Or type:

python
Copy
Edit
quit()
Line Editing Features
On systems supporting the GNU Readline library, the interpreter supports interactive editing, history, and code completion.

Press Control-P at the prompt:

If it beeps: command-line editing is available.

If ^P is shown or nothing happens: editing isn't available.

Modes of Operation
Interactive mode: If input is from a terminal (TTY), the interpreter reads and executes commands interactively.

Script mode: If a file is passed as an argument, the interpreter executes the script.

Examples:

bash
Copy
Edit
python3.13 script.py
python3.13 -c "print('Hello, world!')"
python3.13 -m module_name
python3.13 -i script.py  # Runs script, then enters interactive mode
All command-line options are detailed in: Command line and environment.
2.1.1 Argument Passing
When running a script, the script name and any additional arguments are available in sys.argv from the sys module:

python
Copy
Edit
import sys
print(sys.argv)
Notes:

The list always has at least one element.

If no script is given: sys.argv[0] is "".

If script is - (standard input): sys.argv[0] is "-".

If -c command is used: sys.argv[0] is "-c".

If -m module is used: sys.argv[0] is the full module name.

Arguments after -c or -m are left in sys.argv.

2.1.2 Interactive Mode
When reading from a TTY, the interpreter enters interactive mode:

bash
Copy
Edit
python3.13
Output:

csharp
Copy
Edit
Python 3.13 (default, April 4 2023, 09:25:04)
[GCC 10.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
Continuation lines are prompted with ...:

python
Copy
Edit
>>> the_world_is_flat = True
>>> if the_world_is_flat:
...     print("Be careful not to fall off!")
Output:

vbnet
Copy
Edit
Be careful not to fall off!
2.2 The Interpreter and Its Environment
2.2.1 Source Code Encoding
Python source files are UTF-8 by default. This supports most languages for use in strings, comments, and identifiers.

To declare a different encoding, add this at the top of your file:

python
Copy
Edit
# -*- coding: encoding -*-
Example using Windows-1252:

python
Copy
Edit
# -*- coding: cp1252 -*-
If the file starts with a Unix shebang line (#!), place the encoding on the second line:

python
Copy
Edit
#!/usr/bin/env python3
# -*- coding: cp1252 -*-