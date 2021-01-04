# Recebe 2 listas e retorna uma que é o resultado da diferença ponto a ponto entre as duas 
import operator

scalar_mult = lambda l1, l2 : sum(map(operator.mul, l1, l2))

map_list_of_lists = lambda f, *mats : list(map((lambda *linhas : list(map(f, *linhas))), *mats))
mult_list_by_escalar = lambda k, l : map((lambda x : x * k), l)
matricial_add = lambda l1, l2 : map(operator.add, l1, l2)
matricial_mult = lambda mat, x : list(map((lambda l : mult_pnt_a_pnt(l, x)), mat))
