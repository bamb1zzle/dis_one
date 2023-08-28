# List Functions
# .sort(key, reverse) and sorted(list,key,reverse)
# Default sort returns ascending order.

m = list(map(lambda x: x*2, [1, 2, 3, 4]))
print(sorted(m, reverse=True))


def sortbySecondElement(x):
    return x[1]


a = [(1, 2), (3, 1), (5, 10), (11, -3)]
a.sort(key=sortbySecondElement)
print(a)


# sorts second param

# sorting using custom key
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

# custom functions to get employee info


def get_name(employee):
    return employee.get('Name')


def get_age(employee):
    return employee.get('age')


def get_salary(employee):
    return employee.get('salary')


# sort by name (Ascending order)
employees.sort(key=get_name)
print(employees, end='\n\n')

# sort by Age (Ascending order)
employees.sort(key=get_age)
print(employees, end='\n\n')

# sort by salary (Descending order)
employees.sort(key=get_salary, reverse=True)
print(employees, end='\n\n')


# Sorting list of tuples according to a key
def middle(n):
    return n[1]

# function to sort the tuple


def sort(list_of_tuples):
    return sorted(list_of_tuples, key=middle)


# driver code
# listoftuples #thats why we cant call
list_ = [(34, 21, 56), (24, 12, 32), (42, 34, 42), (27, 11, 32)]
m = sorted(list_, key=(lambda x: x[2], list_))
print(m)


# Using Bubble Sort
# Bubble sort is just a sorting algorithm for sorting a list of any number of elements. If the adjoining item in a given list are in the incorrect order, it swaps them. It then repeats this process until all of the elements have been sorted.

# In this example, we'll use the bubble sort algorithm to sort a list of tuples.

# Input

# roll = [('Arshia', 26), ('Itika', 53), ('Peter', 82), ('Parker', 74), ('MJ', 45)]
# first = 0
# last = len(roll)
# for k in range(0, last):
#     for l in range(0, last-k-1):
#         if (roll[l][first] > roll[l + 1][first]):
#             new_item = roll[l]
#             roll[l]= roll[l + 1]
#             roll[l + 1]= new_item
# print(roll)
# Output:

# [('Arshia', 26), ('Itika', 53), ('MJ', 45), ('Parker', 74), ('Peter', 82)]

# https://www.javatpoint.com/how-to-sort-tuple-in-python#:~:text=In%20Python%2C%20use%20the%20sorted,type%20to%20a%20tuple%20().
# n = 1 # N. . .
# [x[n] for x in elements]

# I think the reason why map still exists at all when generator expressions also exist, is that it can take multiple iterator arguments that are all looped over and passed into the function:

# >>> list(map(min, [1,2,3,4], [0,10,0,10]))
# [0,2,0,4]
# That's slightly easier than using zip:

# >>> list(min(x, y) for x, y in zip([1,2,3,4], [0,10,0,10]))
# Otherwise, it simply doesn't add anything over generator expressions.
