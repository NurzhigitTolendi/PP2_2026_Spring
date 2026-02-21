# iterators and generators

# iterators

# https://docs.python.org/3/tutorial/classes.html#iterators

a = [1, 5, 7] # a list, an example of an iterable

a_iter = iter(a) # iterator of the list a

print(next(a_iter)) # 1
print(next(a_iter)) # 5
print(next(a_iter)) # 7

print(next(a_iter)) # error: StopIteration
