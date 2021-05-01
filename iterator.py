from itertools import *

# sliding_window([a0, a1, ..., an], k) = [(a0, a1, ..., ak), (a1, a2, a3, ... a(k+1)), ..., (a(n-k+1), a(n-k+2), ... an)]

# Works for list, everything else might have problems due to competing iterators
sliding_window = lambda n, l : zip(*(islice(l, i, None) for i in range(n)))
# This version solves that by using tee
sliding_window_tee = lambda itbl, n : zip(*(islice(itblc, i, None) for i, itblc in enumerate(tee(itbl, n))))
