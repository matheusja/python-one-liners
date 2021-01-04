import itertools

sliding_window = lambda n, l : zip(*(itertools.islice(l, i, None) for i in range(n)))
