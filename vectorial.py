from operator import *

# scalar_mult([a0, a1, a2, ..., an], [b0, b1, b2, ..., bm]) = a0 * b0  +  a1 * b1  +  a2 * b2  +  ...  + an * bn
# trims the iterable with more values
scalar_mult = lambda l1, l2 : sum(map(mul, l1, l2))


# apply function to list of lists
map_list_of_lists = lambda f, *mats : [[f(entry) for entry in line] for line in mats]
# multiply every element of a iterable by a "scalar" value 'k'
mult_list_by_escalar = lambda k, l : (x * k for x in l)
# add, value by value, two iterable 
# trims the iterable with more values
matricial_add = lambda l1, l2 : map(add, l1, l2)
# matricial multiplication
matricial_mult = lambda mat, x : list(map((lambda l : scalar_mult(l, x)), mat))


from iterator import sliding_window_tee
# convolution_1d([a0, ..., ak], [b0, b1, ... bm]) = [a0*b0+a1*b1+..ak*bk, a0*b1+a1*b2+...+ak+b(k+1), ..., a0*b(m-k)+...+ak*bm]
# Actually cross-correlation
convolution_1d = lambda k, l : (scalar_mult(k, slid_l) for slid_l in sliding_window_tee(l, len(k)))
