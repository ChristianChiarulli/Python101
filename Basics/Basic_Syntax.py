


# Easiest Hello World

print("Hello, Python!");

# You can chmod +x and run with ./

# Python does not use braces or brackets
# Instead uses rigidly enforced indentation

if True:
    print ("True")
    print ("Answer")

else:
    print ("False")
    print ("Answer")

# Multi Line statements

# If you notice adding the \ character will forse another indent when pressing
# enter, if you press enter without them the cursor won't follow the indent

a = 1
b = 2
c = 3

total = a + \
        b + \
        c

print(total)


# Statements conained do not need th line continuation character
# For exaample

days = ['Monday', 'Tuesday',
        'Wednesday', 'Thursday', 'Friday']

print(days)

# pthyon accepts single (') double (") and triple (''' or """) quotes to denote
# string literals, as long as the same type of quote starts and ends the string

word = 'word'

sentence = "This is a sentence."

paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""

# Btw pyhton does not support multi-line comments


# The following line of this program displays the prompt and the statement
# saying "Press the enter key to exit" and waits for the user to take action

input ("\n\nPress the enter key to exit.")

# The \n\n will create to new lines before displaying the text

# The semicolon (;) allows multiple statements on  single line given that no
# statement starts a new code block. For example:

import sys; x = 'foo'; sys.stdout.write(x + '\n')


