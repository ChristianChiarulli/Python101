import sys

# iterator is an object which allows traversal through all elements in a
# collecion regardless of implementation

# use methods iter() and next()

list = [1,2,3,4]

it = iter(list) # builds iterator object
print(next(it))

# traversed using regular for statement

for x in it:
    print (x, end=" ")

# or use next() function

while True:
    try:
        print(next(it))
    except StopIteration
        sys.exit() 



