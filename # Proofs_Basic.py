# Proof that strings are immutable
string = "Hello"
print(string)
string[0] = "h"
print(string) # Error: 'str' object does not support item assignment

# Proof that integers are immutable
a = 10
print(a)
a = 20
print(a)

# Proof that floats are immutable
b = 10.5
print(b)
b = 20.5
print(b)

# Proof that booleans are immutable
c = True
print(c)
c = False
print(c)

# Proof that None is immutable
d = None
print(d)
d = 10
print(d)

# Proof that lists are mutable
list = [1, 2, 3, 4, 5]
print(list)
list[0] = 10
print(list)

# Proof that tuples are immutable
tuple = (1, 2, 3, 4, 5)
print(tuple)
tuple[0] = 10
print(tuple) # Error: 'tuple' object does not support item assignment

# Proof that sets are mutable
set = {1, 2, 3, 4, 5}
print(set)
set.add(6)
print(set)

# Proof that dictionaries are mutable
dictionary = {"a": 1, "b": 2, "c": 3}
print(dictionary)
dictionary["a"] = 10
print(dictionary)

# Proof that functions are mutable
def func():
    print("Hello")
func()
func = 10
print(func)

# Proof that classes are mutable
class Class:
    def __init__(self):
        print("Hello")
obj = Class()
obj = 10
print(obj)

# Proof that modules are mutable
import math
print(math.pi)
math = 10
print(math)

# Proof that packages are mutable
import os
print(os.getcwd())
os = 10
print(os)

# Proof that files are mutable
file = open("file.txt", "w")
file.write("Hello")
file.close()
file = 10
print(file)

# Proof that directories are mutable
import os
os.mkdir("directory")
os.rmdir("directory")
directory = 10
print(directory)
