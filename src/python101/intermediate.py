# condtions (I already know if,else,elif,nested if)

#ternary operator
number  = int(input("Enter a number: "))
result = f"{number} is odd" if number%2 != 0 else f"{number} is even"
print(result)

# in and not in operator
vowels = "aeiou"
char = "a"

if char in vowels:
    print(f"{char} is a vowel.") # Output: a is a vowel.
else:
    print(f"{char} is not a vowel.")
    
    
# enumerate () -> more useful for keeping track of frequencies 
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")
# Output:
# Index: 0, Fruit: apple
# Index: 1, Fruit: banana
# Index: 2, Fruit: cherry

# The zip() function allows you to iterate over multiple sequences in parallel. It combines elements from each sequence into tuples.
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 28]

for name, age in zip(names, ages):
    print(f"Name: {name}, Age: {age}")
# Output:
# Name: Alice, Age: 25
# Name: Bob, Age: 30
# Name: Charlie, Age: 28