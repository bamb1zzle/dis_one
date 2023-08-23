# leetcode 49: group anagrams
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # assign all these letters as one value with a key
        # for each key we are adding to the hash map we want each value to be a list.
        anagram_map = defaultdict(list)
        result = []

        for s in strs:
            sorted_s = tuple(sorted(s))  # sorted_s key = sorted s
            # append original s to the sorted s key.
            anagram_map[sorted_s].append(s)
# when you run sorted on a string. you are getting a list object back but that is mutable. mutable data types cannot be keys.
        for value in anagram_map.values():
            result.append(value)

        return result

    print(result)


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
groupAnagrams(strs)

# initialize the hashmap
# identify what the key will be and what the values will be
# assign it in the hashmap
