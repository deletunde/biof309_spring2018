# map(function_to_apply, list_of_inputs)
# map(func, iterable1, iterable2)
items = [1, 2, 3, 4, 5]
squared1 = []
for i in items:
    squared1.append(i**2)
squared1

items = [1, 2, 3, 4, 5]
squared2 = list(map(lambda x: x**2, items))
squared2 

items = [1, 2, 3, 4, 5]
squared3 = [x**2 for x in items]
squared3 

squared3g = ( x**2 for x in items )
list( squared3g )

## which of the above is faster?

# use map when list comprehension would be too complicated
def add(x):
    return (x+x)
def subtract(x):
    return (x-x)
def square(x):
    return (x**2)
def sqrt(x):
    return (x**(1/2))
def multiply(x):
    return (x*x)
# dividing by zero returns an error
#def divide(x):
#    return (x/x)
funcs = [multiply, add, square, sqrt]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)
# Turn the following map functions into list comprehensions

# Return double of n
def addition(n):
    return n + n
# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# Double all numbers using map and lambda
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

# Add two lists using map and lambda

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

# List of strings
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = list(map(list, l))
print(test)

