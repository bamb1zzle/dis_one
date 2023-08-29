# List Functions
# .sort(key, reverse) alters original list. and sorted(list,key,reverse) creates new list.
# Default sort returns ascending order. If reverse = True, returns descending order.

from operator import itemgetter

m = list(map(lambda x: x*2, [1, 2, 3, 4]))
print(sorted(m, reverse=True))

mapList = [[50], ["hi"], [True]]
print(list(map(tuple, mapList)))

# tuple function defaults 1 element
# iterate lists using loops or map function
# list comprehenision initializes new list and values at same time.


def sortbySecondElement(x):
    return x[1]


a = [(1, 2), (3, 1), (5, 10), (11, -3)]
a.sort(key=sortbySecondElement)
print(a)


list_ = [(34, 21, 56), (24, 12, 32), (42, 34, 42), (27, 11, 32)]
print(sorted(list_, key=lambda x: x[2]))
list_.sort(key=lambda x: x[1])
print(list_)

teams = [
    {'Team': 'Dignitas', 'Members': 5, 'Salary': 100000},
    {'Team': 'Team Liquid', 'Members': 5, 'Salary': 500000},
    {'Team': 'Team Secret', 'Members': 5, 'Salary': 200000},
    {'Team': 'Navi', 'Members': 5, 'Salary': 150000},
]


def team_name(team):
    return team.get('Team')


def salary(team):
    return team.get('Salary')


teams.sort(key=team_name)
print(teams, end='\n')

# sort by salary (Descending order)
teams.sort(key=salary, reverse=True)
print(teams, end='\n')


# Bubble Sorting - Sorting algorithm for sorting a list of any number of elements. Compares first and second elements and swaps elements around in the correct order using one loop. And carries that on for all remaining iterators.
payRoll = [('Andy', 80000), ('Jessica', 50000),
           ('James', 45000), ('Ash', 100000)]
pay = 1
full = len(payRoll)
# Initialize the value we want to sort by and the list size for our loop
for k in range(0, full):  # First loop for every value
    # Second loop for passing x value to its correct position in the list.
    for l in range(0, full-k-1):
        if (payRoll[l][pay] > payRoll[l+1][pay]):
            saveInfo = payRoll[l]  # Save information of greater value
            # Switch the lesser value to the greater values place.
            payRoll[l] = payRoll[l+1]
            # The next index is now the greater value that was saved earlier.
            payRoll[l+1] = saveInfo
print(payRoll)


# List comprehension is defined inside square brackets [ ]. This reminds us that the resulting object is definitely a list.
# zip() = returns list of tuples. used to combine lists of tuples.
# list(zip(list))

lst1 = [10, 20, 30]
lst2 = [50, "Python", "JournalDev"]
lsit_tuple = list(zip(lst1, lst2))
print(lsit_tuple)

newlist = ["eat", "sleep", "repeat"]
newlist.insert(1, "train")
print(newlist)

l = [(21, "John", True), ("Jackson", 22, False), ("Mayweather", False, 20)]
# When comparing different data types cant use > so have to do by datatype itself.
print(sorted(l, key=str))


print(itemgetter(1)((2, 5, 3)))


g = list(map(min, [1, 2, 3, 4], [0, 10, 0, 10]))
print(g)
# map takes multiple iterator arguments that are all looped over and passed into the function vs generator
h = list(min(x, y) for x, y in zip([1, 2, 3, 4], [0, 10, 0, 10]))
print(h)
