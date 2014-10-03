# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

print 'Rewriting Filter, Reduce, and Map:'

odd_num = lambda x: x % 2 != 0
even_num = lambda x: x % 2 == 0
len_4_list = lambda x: len(x) >= 4


def new_filter(function, list):
	new_list = []
	for item in list:
		if function(item) == True:
			new_list.append(item)
	return new_list

print new_filter(odd_num, number_list)
print new_filter(even_num, number_list)
print new_filter(len_4_list, word_list)
print '********************************'

smallest = lambda x, y: x if x < y else y
largest = lambda x, y: x if x > y else y
sums = lambda x, y: x + y
multiplies = lambda x, y: x * y
join_strings = lambda x, y: x + ' ' + y

def new_reduce(function, list):
	return_value = list[0]
	for item in list[1:]:
		return_value = function(return_value, item)
	return return_value

print new_reduce(smallest, number_list)
print new_reduce(largest, number_list)
print new_reduce(sums, number_list)
print new_reduce(multiplies, number_list)
print new_reduce(join_strings, word_list)

print '********************************'

halvsies = lambda x: x / 2.0
word_length = lambda x: len(x)

def new_map(function, list):
	new_list = []
	for item in list:
		new_list.append(function(item))
	return new_list

print new_map(halvsies, number_list)
print new_map(word_length, word_list)
