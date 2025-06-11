# data types

# note: Python integers have arbitrary precision, meaning they can represent numbers of any size, limited only by available memory. This is a significant advantage over languages like C++ or Java, where integers have fixed sizes (e.g., 32-bit or 64-bit).

import sys

# Raise the limit to something higher, like 1 million digits
sys.set_int_max_str_digits(1000000)

large_no = 9**999
print(large_no)

float_no = 0.1 + 0.2  # not accurate decimal
print(float_no)

# Using the decimal module for precise calculations
from decimal import Decimal

print(Decimal('0.1')+Decimal('0.2'))


# to work with fractional stuff

from fractions import Fraction
num1 = Fraction(1,3)
num2 = Fraction(2,5)
print(num1+num2)


#complex numbers

z = 10 + 5j  # here we are using j as img part, as per engineering. because i is not used since i is actually for current
print(z.real)
print(z.imag)
print(abs(z))

#strings (f*cking important)

#note: Python 3 uses Unicode (UTF-8 by default) for representing strings, which supports a wide range of characters from different languages

text = "你好，世界"  #english is not used here coz, utf-8 will anyways encode english and other numerics in 1 byte. Characters outside the ASCII range (like characters from non-Latin scripts such as Chinese, Japanese, or accented letters) are encoded in multiple bytes

encoder = text.encode('utf-8')
print(encoder)
print(encoder.decode('utf-8'))


# string formatting (just like template literals in js)
name  = "Sanjay"
goal = "Learn AI, python in depth"
message = f"Hola!, I'm {name} my goal is to {goal}"
print(f"This is the f*cking message i wanna tell \n{message}")


#regex (pretty irritating, but only fundamentals, anyway will use online tool to build patterns if need in future)
import re
phrase = "We are the followers of the Great Warrior Mr. Velupillai Prabhakaran"
"""

The r"" notation represents a raw string literal in Python.

Without r: Python will interpret special characters like backslashes (\) as escape sequences (e.g., \n for newline, \t for tab). So if you write a regular expression like \b\w{3}\b, Python will treat \b as a backspace character and \w as a single word character. This is not what you want in regex.

With r: By using r"", you create a raw string where backslashes are treated as literal characters, meaning they are not escaped. So r"\b\w{3}\b" will correctly match word boundaries and word characters.

"""
pattern = r"followers"
match = re.search(pattern,phrase)
if match:
    print("match found", match.group())
else:
    print("Match not found")
    
pattern = r"\b\w{3}\b" # Matches 3-letter words
matches = re.findall(pattern, phrase)
print(matches) 


# Boolean (pretty easy, so not gonna focus that depth)
x = 5
y = 10
if x > 0 and y < 20:
    print("Both conditions are true")

if x < 0 or y > 5:
    print("At least one condition is true")

if not x == y:
    print("x is not equal to y")



