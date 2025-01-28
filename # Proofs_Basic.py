# Proof that strings are immutable
string = "Hello"
print(string)
string[0] = "h"
print(string) # Error: 'str' object does not support item assignment

# Proof that lists are mutable
list = [1, 2, 3, 4, 5]
print(list)
list[0] = 10
print(list)
