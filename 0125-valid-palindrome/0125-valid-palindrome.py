class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        s = ''.join(i.lower() for i in s if i.isalnum())
        for i in s:
            
            stack.append(i)
        for i in s:
            if stack[-1] == i :
                stack.pop()
        if stack:
            return False
        return True
        