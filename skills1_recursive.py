'''Rewriting the filter, reduce, and map functions recursively.'''

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

print 'Rewriting Filter, Reduce, and Map:'

odd_num = lambda x: x % 2 != 0
even_num = lambda x: x % 2 == 0
len_4_list = lambda x: len(x) >= 4


def filter_recursive(function, list_passed):
    if list_passed == []:
        return list_passed
    else:
        if function(list_passed[0]):
            return [ list_passed[0] ] + filter_recursive(function, list_passed[1:])
        else:
            return filter_recursive(function, list_passed[1:])


print filter_recursive(odd_num, number_list)
print filter_recursive(even_num, number_list)
print filter_recursive(len_4_list, word_list)
print '********************************'

smallest = lambda x, y: x if x < y else y
largest = lambda x, y: x if x > y else y
sums = lambda x, y: x + y
multiplies = lambda x, y: x * y
join_strings = lambda x, y: x + ' ' + y

def reduce_recursive(function, list_passed):
    if len(list_passed) == 1:
        return list_passed[0]
    elif list_passed == []:
        return None
    else:
        return function(list_passed[0], (reduce_recursive(function, list_passed[1:])))

print reduce_recursive(smallest, number_list)
print reduce_recursive(largest, number_list)
print reduce_recursive(sums, number_list)
print reduce_recursive(multiplies, number_list)
print reduce_recursive(join_strings, word_list)

print '********************************'

halvsies = lambda x: x / 2.0
word_length = lambda x: len(x)

def map_recursive(function, list_passed):
    if list_passed == []:
        return list_passed
    else:
        return [ function(list_passed[0]) ] + map_recursive(function, list_passed[1:])

print map_recursive(halvsies, number_list)
print map_recursive(word_length, word_list)





