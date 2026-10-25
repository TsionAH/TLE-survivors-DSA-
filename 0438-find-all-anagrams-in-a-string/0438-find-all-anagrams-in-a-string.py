from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        target = Counter(p)
        
        n = len(p)
        left = 0
        anagram = []
        while n <= len(s):
            check = s[left:n]
            check = Counter(check)
            if check == target:
                anagram.append(left)
            left += 1
            n += 1
        return anagram