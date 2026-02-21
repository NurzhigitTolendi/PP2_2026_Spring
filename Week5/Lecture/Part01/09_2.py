# iterators and generators

# generators

# https://docs.python.org/3/tutorial/classes.html#iterators

def nums():
    start = 1
    while(start < 10):
        yield start
        start += 1

for num in nums():
    print(num)