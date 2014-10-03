# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

print 'Using Filter, Reduce, and Map:'
# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
print filter((lambda x: x % 2 != 0), number_list)

# Write a function that takes a list of numbers and returns a new list with only the even numbers.
print filter((lambda x: x % 2 == 0), number_list)

# # Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
print filter((lambda x: len(x) >= 4), word_list)

# # Write a function that finds the smallest element in a list of integers and returns it.
print reduce(lambda x, y: x if x < y else y, number_list)

# # Write a function that finds the largest element in a list of integers and returns it.
print reduce(lambda x, y: x if x > y else y, number_list)

# # Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
print map((lambda x: x / 2.0), number_list)

# # Write a function that takes a list of words and returns a list of all the lengths of those words.
print map((lambda x: len(x)), word_list)

# # Write a function (using iteration) that sums all the numbers in a list.
print reduce((lambda x, y: x + y), number_list)

# # Write a function that multiplies all the numbers in a list together.
print reduce((lambda x, y: x * y), number_list)

# # Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
print reduce((lambda x, y: x + ' ' + y), word_list)

# # Write a function that takes a list of integers and returns the average (without using the avg method)
print reduce((lambda x, y: x + y), number_list) / len(number_list)

print '\n'

print 'Using List Comprehension:'

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
print [x for x in number_list if x % 2 != 0]

# Write a function that takes a list of numbers and returns a new list with only the even numbers.
print [x for x in number_list if x % 2 == 0]

# # Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
print [x for x in word_list if len(x) >= 4]

# # Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
print [x / 2.0 for x in number_list]

# # Write a function that takes a list of words and returns a list of all the lengths of those words.
print [len(x) for x in word_list]