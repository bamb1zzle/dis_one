city_map = {}

cities = ["Calgary", "Vancouver", "Toronto"]
# first must need to initialize this key because it doesnt exist in hashmap yet.
city_map["Canada"] = []
city_map["Canada"] += cities
# Dictionary: All keys need to be initialized
# DefaultDict: All keys are already initialized
print(city_map["Canada"])

# Coding Hashamps: Retrieving Data
# hashmap.keys() - returns all keys in form of list
# hashamp.values () - returns all the values in list
# hashmap.items() - returns combo as a list.
