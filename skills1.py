# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
    odd_list = []
    for item in number_list:
        if item % 2 != 0:
            odd_list.append(item)
    return odd_list

# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    even_list = []
    for item in number_list:
        if item % 2 == 0:
            even_list.append(item)
    return even_list

# # Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    len_4_words = []
    for item in word_list:
        if len(item) >= 4:
            len_4_words.append(item)
    return len_4_words

# # Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
    lowest_num = number_list[0]
    for item in number_list:
        if item <= lowest_num:
            lowest_num = item
    return lowest_num

# # Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    highest_num = number_list[0]
    for item in number_list:
        if item >= highest_num:
            highest_num = item
    return highest_num

# # Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    divided_list = []
    for item in number_list:
        divided_list.append(item / 2.0)
    return divided_list

# # Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    length_of_words = []
    for item in word_list:
        length_of_words.append(len(item))
    return length_of_words

# # Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    sum = 0
    for item in number_list:
        sum += item
    return sum

# # Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    product = 1
    for item in number_list:
        product *= item
    return product

# # Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
    s = ''
    for item in word_list:
        s += (item + ' ')
    return s

# # Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    sum = 0
    for item in number_list:
        sum += item
    average_of_list = sum / len(number_list)
    return average_of_list
