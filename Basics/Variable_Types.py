# Python variables do not need explicit declaration to reserve memory space 

counter = 100   # An integer assignment
miles = 1000.0  # A floating point
name = "John"   # A string

print(counter)
print(miles)
print(name)

# Multiple Assignment

# all assigned to same number
a = b = c = 1

# Assign multiple objects to multiple variables

a, b, c = 1, 2, "Tom"

# Standard Data Types

# Python has 5

# Numbers
# String
# List
# Tuple
# Dictionary

### NUMBERS ###

var1 = 1
var2 = 10

# You can also delete reference to a number by using the del statement 
del var1

# Python supports three different numberical types

# int (signed integers), float (real values), complex (complex numbers)

# all numbers are represented as long integers in Python3

### STRINGS ###

# * is the repetition operator and + is the concatonation operator

str = 'Hello World'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string

### LISTS ###

# Lists are the most versaltiel of Pythons compound data types
# Items belonging to a list 
# You can add new items to a list

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)          # Prints complete list
print (list[0])       # Prints first element of the list
print (list[1:3])     # Prints elements starting from 2nd till 3rd 
print (list[2:])      # Prints elements starting from 3rd element
print (tinylist * 2)  # Prints list two times
print (list + tinylist) # Prints concatenated lists

### TUPLES ###

# Tuples can be thought of as read only lists

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)           # Prints complete tuple
print (tuple[0])        # Prints first element of the tuple
print (tuple[1:3])      # Prints elements starting from 2nd till 3rd 
print (tuple[2:])       # Prints elements starting from 3rd element
print (tinytuple * 2)   # Prints tuple two times
print (tuple + tinytuple) # Prints concatenated tuple

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
#tuple[2] = 1000    # Invalid syntax with tuple
list[2] = 1000     # Valid syntax with list

### DICTIONARY ###

# Dictionaries are a kind hash table, they consist of key value pairs

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values

# Data Type conversion

#int(x [,base])

#Converts x to an integer. The base specifies the base if x is a string.

#float(x)

#Converts x to a floating-point number.

#complex(real [,imag])

#Creates a complex number.

#str(x)

#Converts object x to a string representation.

#repr(x)

#Converts object x to an expression string.

#eval(str)

#Evaluates a string and returns an object.

#tuple(s)

#Converts s to a tuple.

#list(s)

#Converts s to a list.

#set(s)

#Converts s to a set.

#dict(d)

#Creates a dictionary. d must be a sequence of (key,value) tuples.

#frozenset(s)

#Converts s to a frozen set.

#chr(x)

#Converts an integer to a character.

#unichr(x)

#Converts an integer to a Unicode character.

#ord(x)

#Converts a single character to its integer value.

#hex(x)

#Converts an integer to a hexadecimal string.

#oct(x)

#Converts an integer to an octal string.
