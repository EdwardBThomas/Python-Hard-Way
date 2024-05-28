from sys import argv 
"""
An 'import' adds user-defined features from the Python library to 
save space. The argv is an 'argument variable' that holds arguments
passed to the Python script. In this context, features are modules are 
libraries.
read the WYSS section for how to run this
"""
script, first, second, third = argv
"""
This line unpacks argv so that rather than holding all the arguments, 
it gets assigned the four variables described in the script.
In summary, the script says 'take whatever is in argv, unpack it, and 
assign it to these variables on the left in order.'
"""

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)