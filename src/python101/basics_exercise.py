"""
Exercises

1. Floating-Point Precision: Write a function that takes two floating-point numbers as input and checks if they are approximately equal within a given tolerance (e.g., 1e-6).

2. String Manipulation: Write a function that takes a string as input and returns a dictionary containing the frequency of each word in the string. Use regular expressions to remove punctuation and convert the string to lowercase.

3. List Comprehension and Filtering: Given a list of numbers, use list comprehension to create a new list containing only the numbers that are divisible by both 2 and 3.
4. Dictionary and Set Operations: You have two lists of user IDs: active_users and inactive_users. Convert them to sets and find the users who are in both lists (i.e., users who were once active but are now inactive).≈
"""

"""
solution: using abs here coz, we don't need signs ()-ve or +ve which can impact the results, since we are checking for the tolerance only. i.e the difference is less that 1e-6 or not, so if the overall dif is in neg, it blindly says out of tolerance which negates the purpose.
here we can use Decimal object, i.e Decimal('num'), this will be more accurate, but in production we will not use this mostly becuase it comes with cost. unlike float it is software dependant which makes it more slower
    
"""
def floating(num1,num2):
    if abs(num1-num2) <= 1e-6:
        print("Within given tolerance")
    else:
        print("Out of tolerance")
        
floating(1.89,20.78)


import re
def string_frequency(phrase):
    pattern = r'\b\w+\b'
    cleaned_phrase = re.findall(pattern,phrase.lower())
    print(cleaned_phrase)
    frequency = {}
    
    # not dict comprehension coz, comprehension is useful for single iteration or single visit of the elements, for multiple iterations like counting stuff, for loop makes more sense and efficient
    for word in cleaned_phrase:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    print(frequency)

string_frequency("Hello how are you?, Hello, hello hello")


my_numbers = [1,2,3,4,5,6,7]
div_numbers = [num for num in my_numbers if num % 2 == 0 and num % 3 == 0]
print(div_numbers)

# Lists of user IDs
active_users = [10, 20, 30, 40, 50, 60]
inactive_users = [55, 65, 85, 10, 20, 40]

# Convert lists to sets
active_users_set = set(active_users)
inactive_users_set = set(inactive_users)

# Find users who are in both active and inactive sets
both = active_users_set.intersection(inactive_users_set)

# Print the result
print(both)