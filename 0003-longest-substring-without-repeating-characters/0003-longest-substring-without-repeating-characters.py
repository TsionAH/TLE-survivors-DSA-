class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        my_set = set()
        max_count = 0
        start = 0
        end = start 
        while end < len(s):
           
            
           
            if s[end] not in my_set:
                my_set.add(s[end])
                end += 1
                max_count = max(max_count,end-start)
            else:
                my_set.remove(s[start])

                start += 1
        return max_count