
# Partially applied a function to the 'x' positional arguments and 'k' keyworded arguments
# print2 = partial(print, end='')
# print2 is a function that prints without adding anything on the end(contrast with newline)
# note that keyworded arguments applied to the resulting function have precedence over partially applied ones, so print2("Something", end='\n') will print "Something" and put a newline
partial = lambda f, *x, **k : lambda *y, **l : f(*x, *y, **{**k, **l})
