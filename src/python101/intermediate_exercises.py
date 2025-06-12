"""
Data Processing with List Comprehensions: You have a list of sentences. Use list comprehensions to create a new list containing the lengths of each sentence, but only for sentences that contain the word "AI".

"""
sentences = ["Hello, I'm AI", "AI is good", "Sanjay is engineer"]
ai_sentence_lengths = [len(sentence) for sentence in sentences if "AI" in sentence]

print(ai_sentence_lengths)



"""
Dictionary Comprehension for Data Transformation: You have a list of tuples, where each tuple contains a product name and its price. Use a dictionary comprehension to create a dictionary where the keys are the product names and the values are the prices, but only for products with prices greater than 1000 rs.

"""
shop = [('Rc Helicopter', 1200), ('Blazer', 7000), ('Chocos', 20), ('Cloud Nine Pizza', 700)]

# Use dictionary comprehension to filter products with price greater than ₹10
filtered = {product[0]: product[1] for product in shop if product[1] > 10}

print(filtered)


