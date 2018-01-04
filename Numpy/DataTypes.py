import numpy as np

# Numpy supports a much greater variety of numerical types than Python does

# dtype is constructed as follows:

# numpy.dtype(object, align, copy)

# using array-scalar type

dt = np.dtype(np.int32)

print(dt)

#int8, int16, int32, int64 can be replaced by equivalent string 'i1','i2','i4', etc. 

dt1 = np.dtype('i1')

print(dt1)

# using endian notation

# '<' means that encoding is little-endian (least significant is stored in smallest address)

# '>' means that encoding is big-endian (most significant byte is stored in smallest address)

dt2 = np.dtype('>i2')

print(dt2)

# The following examples will show the use of a structured data type

# first create structured data type

dt3 = np.dtype([('age', np.int8)])

print(dt3)

# now apply it to ndarray object

dt4 = np.dtype([('age', np.int8)])

a = np.array([(10,),(20,),(30,)], dtype = dt4)

print(a)

# file name can be used to acess content of age column

print(a['age'])

## The following example defines a structured data type called student with a
# field 'name', an integer field 'age' and a float field 'marks'

# the dtype is applied to an ndarra object

student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
b = np.array([('John', 21, 50),('Tom', 18, 75)], dtype = student)
print(b)
