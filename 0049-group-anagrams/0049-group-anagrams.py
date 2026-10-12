from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        my_map = defaultdict(list)
        result = []
        for i in strs:
            my_sort = tuple(sorted(i))
            my_map[my_sort].append(i)
        for i in my_map.values():
            result.append(i)
        return result

        