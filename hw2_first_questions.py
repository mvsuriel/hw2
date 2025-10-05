# 1)
# Create a function named
# "triple" that takes one
# parameter, x, and returns
# the value of x multiplied
# by three.

def triple (x): 
    return x * 3
print(triple(2)) #this should return 3
print(triple(8)) #this should return 24
print(triple(12))#this should return 36

# 2)
# Create a function named "subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.

def subtract (a,b): 
    return a-b 
print (subtract(50,18)) #this should return 32
print (subtract(200,81))#this should return 119
print (subtract(8,15))#this should return -7

# 3)
# Create a function called "dictionary_maker"
# that has one parameter: a list of 2-tuples.
# It should return the same data in the form
# of a dictionary, where the first element
# of every tuple is the key and the second
# element is the value.

# For example, if given: [('foo', 1), ('bar', 3)]
# it should return {'foo': 1, 'bar': 3}
# You should program the function and not use
# the function "dict" directly

#def dictionary_maker (key,value): 
    #return {key: value}

def dictionary_maker(tuples):
    result = {}
    for key, value in tuples:
        result[key] = value
    return result

print(dictionary_maker([('foo', 1), ('bar', 3)]))
print(dictionary_maker([('Majo','Colombia'), ('Elvis','Honduras'), ('María','Dominicana')]))

