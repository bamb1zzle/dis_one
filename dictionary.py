from collections import defaultdict

basicDict = dict()  # Initialized Dictionary // dict()
# Created key with value(empty list) Append value to key. Due to value being list type must use append.

# Pushing multiple key:value pairs into dictionary
basicDict = {1: "two", 2: "three"}
testValues = ["a", "b", "c", "d"]  # Assigning values to variable.
# Created key "default" and assigned our variable(values) to it.
basicDict["default"] = testValues
basicDict["empty"] = []
basicDict["empty"].append(9)
basicDict["simplePush"] = 5  # Simple key:value pair created using subscript.

# Watch out for assigning new lists. It will overwrite the previous data.

print(basicDict.keys())
print(basicDict["default"])
print(basicDict["empty"])
print(basicDict["simplePush"])
print(basicDict.values())

# .values() and .keys() return all of the key & values in a list form.


# Default Dictionary // from collections import defaultdict // defaultdict(arguement)
def defaultValue():
    return -1
# Define arguement to give default value that will be passed through defaultdict()


# initialize dictionary with default arguement.
newDict = defaultdict(defaultValue)

newDict["test1", "test2", "test3"]  # commas don't create multiple keys.

newDictAdd = {'test4': 5, 'test5': 6}
newItAdd = (('test6', 7), ('test7', 8))

newDict.update(newDictAdd)  # Update by passing dictionary
newDict.update(newItAdd)  # Update by passing iterables
newDict.update(test8=9, test9=10)  # Pass as Keyword Arguements
print(newDict.items())

j = 0

for i in newDict:
    j += 1

print("The amount of items in your dictionary is currently: ", j)


# Dictionary: All keys need to be initialized
# DefaultDict: All keys are already initialized
# Coding Hashamps: Retrieving Data
# hashmap.keys() - returns all keys in form of list
# hashamp.values () - returns all the values in list
# hashmap.items() - returns combo as a list.
