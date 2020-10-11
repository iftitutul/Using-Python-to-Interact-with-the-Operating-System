### Data Streams

How does a Python program connect to both the screen and the keyboard? Well, it uses I/O streams. 

I/O streams are the basic mechanism for performing input and output operations in your programs. You can think of these streams as pathways between your programs and their input sources like a keyboard, or output, like the screen. I/O streams aren't just available for Python programs. When we run a system command on our terminal, I/O streams are also being used to connect that command to the terminal input and output. This way, we can see the results of the command or enter data interactively if that's how the program works. We call these streams because the data keeps flowing. A program can read input and generate output as long as it needs to achieve its goal. 

Okay, what do these streams mean in practice? Most operating systems supply three different I/O streams by default each with a different purpose.
- **STDIN:** The standard input stream commonly referred to as STDIN is a channel between a program and a source of input. Usually in the form of text data from the keyboard. When we use the input function to accept user input in a Python script we're using the STDIN stream.
- **STDOUT:** The standard output stream or STDOUT is a pathway between a program and a target of output, like a display. STDOUT generally takes the form of text displayed in a terminal. As that play when we use the print function to write information to the screen.
- **STDERR:** The last type of pre-made I/O stream is called standard error, or STDERR. Standard error displays output like standard out, but is used specifically as a channel to show error messages and diagnostics from the program. It's usually printed to the screen. If you've ever run some Python code and receive an error, then that error message was probably printed using standard error stream.

### Summary

Python 2 and Python 3 handle input and raw_input differently.

### In Python 2

- input(x) is roughly the same as eval(raw_input(x))
- raw_input() is preferred, unless the author wants to support evaluating string expressions.
- eval() is used to evaluate string expressions.

Standard Library Docs:

- https://docs.python.org/2/library/functions.html#input
- https://docs.python.org/2/library/functions.html#raw_input
- https://docs.python.org/2/library/functions.html#eval

### In Python 3

- Input handles string as a generic string. It does not evaluate the string as a string expression.
- raw_input doesn’t exist, but with some tricky techniques, it can be supported.
- eval() can be used the same as Python 2.

Standard Library Docs: 

- https://docs.python.org/3/library/functions.html#input
- https://docs.python.org/3/library/functions.html#eval

### Python Subprocesses Cheat Sheet
Check out the following link for more information:

- https://docs.python.org/3/library/subprocess.html
