class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        if not s:
            return 0
        left = 0
        right = 0
        max_range = 0
        while right < len(s):
            if s[right] not in check:
                check.add(s[right])
                right += 1
                max_range = max(max_range,right-left )
            else:
                check.remove(s[left])
                left += 1
        return max_range

