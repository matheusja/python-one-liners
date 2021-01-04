import operator import *

# scalar_mult([a0, a1, a2, ..., an], [b0, b1, b2, ..., bm]) = a0 * b0  +  a1 * b1  +  a2 * b2  +  ...  + an * bn
# trims the iterable with more values
scalar_mult = lambda l1, l2 : sum(map(mul, l1, l2))


# apply function to list of lists
map_list_of_lists = lambda f, *mats : list(map((lambda *lines : list(map(f, *lines))), *mats))
# multiply every element of a iterable by a "scalar" value 'k'
mult_list_by_escalar = lambda k, l : map((lambda x : x * k), l)
# add, value by value, two iterable 
# trims the iterable with more values
matricial_add = lambda l1, l2 : map(add, l1, l2)
# matricial multiplication
matricial_mult = lambda mat, x : list(map((lambda l : scalar_mult(l, x)), mat))
