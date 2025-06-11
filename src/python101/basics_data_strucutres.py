# This covers Lists, Tuples, Dictionary and Sets

#List comprehensions

numbers  = [1,2,3,4,5]
squares = []
for i in numbers:
    squares.append(i**2)

print(squares)

#instead of doing this we can simply do
squares = [i**2 for i in numbers]  # more easy i.e do operation for each item in the list
print(squares)

#List Slicing
# Example of list slicing  start : end -> here end will be declared, but while printing it will show only till the before element unlike start
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:5]) # Output: [2, 3, 4]
print(numbers[:5]) # Output: [0, 1, 2, 3, 4]
print(numbers[5:]) # Output: [5, 6, 7, 8, 9]
print(numbers[::2]) # Output: [0, 2, 4, 6, 8] (every other element) list[start:end:step] (step means, how many elements to skip)
print(numbers[::-1]) # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reversed list)


# advanced list operations Map/filter/reduce (just like js)
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Using map to square each number
squares = list(map(lambda x: x**2, numbers))
print(squares)  # Output: [1, 4, 9, 16, 25]

# Using filter to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

# Using reduce to get the sum of all numbers
sum_of_numbers = reduce(lambda x, y: x + y, numbers)  # reduce is nothing but using accumulator and iterating over the array/list for storing the final value in the acc
print(sum_of_numbers)  # Output: 15  (here x is 0 and is iterator i.e 0+1, 1+2, 3+3, 6+4,10+5)

# Using reduce to get the product of all numbers
product_of_numbers = reduce(lambda x, y: x * y, numbers)
print(product_of_numbers)  # Output: 120



#tuples (immutable i.e cannot change values and represented within () )
point = (10,20)
print(point[0])

# best usecase, tuples as dict key in data analysis, geospatial data or even game dev (coordinates), not list coz it is mutable, and since dict key need to be hashed and inmutable, tuples are more better
geospatial_data = {(1.34,9.881):"Chennai",(2.87,7.11):"Madurai"}  #ignore the mag, lat, just random float lol!
print(geospatial_data[(1.34,9.881)])

# dictionary (Key value pair), just like hashmap (maps in js)
"""
Dictionaries are widely used in AI for:

Representing feature vectors.
Storing mappings between words and their indices in NLP.
Implementing lookup tables.
Caching results of expensive computations.
"""
#Dict comprehension

numbers = [100,200,300,400,500]
square_dict = {key:key**2 for key in numbers} # key:value for key in numbers
print(square_dict)

# dict methods

print(square_dict.get(100)) # besides [] we can use this , just like map has get,set in js
print(square_dict.get(700,70000)) # we can set the value as well for unavailable key


# sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

print(set1.union(set2)) # Output: {1, 2, 3, 4, 5, 6, 7}
print(set1.intersection(set2)) # Output: {3, 4, 5}
print(set1.difference(set2)) # Output: {1, 2}
print(set1.symmetric_difference(set2)) # Output: {1, 2, 6, 7}


