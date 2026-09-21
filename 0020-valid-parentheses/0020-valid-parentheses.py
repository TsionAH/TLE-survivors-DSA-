class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "{([":
                stack.append(i)
            else:
                if not stack:
                    return False
                first = stack.pop()
                if i == ')' and first != '(':
                    return False
                if i == '}' and first != '{':
                    return False
                if i == ']' and first != '[':
                    return False
        return not stack