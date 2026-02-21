# iterators and generators

# generators

# https://docs.python.org/3/tutorial/classes.html#iterators

def our_range(start, stop, step=1):
    if step > 0:
        while(start < stop):
            yield start
            start += step
    elif step < 0:
        while(start > stop):
            yield start
            start += step

for num in our_range(1, 10, 1):
    print(num)

for num in our_range(10, 1, -1):
    print(num)

for num in our_range(10, 20, 0):
    print(num)

