from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = Counter(s)
        count2 = Counter(t)
        if len(t)!= len(s):
            return False
        for i in count:
            if count2[i] != count[i]:
                return False
        return True
       