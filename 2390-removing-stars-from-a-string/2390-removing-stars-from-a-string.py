class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != '*':
                stack.append(s[i])
            else:
                if stack:
                    stack.pop()
        output = ""
        for i in stack:
            output += i
        return output
        
        