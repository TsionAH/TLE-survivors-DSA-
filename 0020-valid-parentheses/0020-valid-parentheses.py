class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '('or i ==  '{' or i ==  '[':
                stack.append(i)
            else:
                if not stack :
                    return False
                up = stack[-1]
                if  up == '(' and i != ')':
                    return False
                elif  up == '{' and i != '}':
                    return False
                elif  up == '[' and i != ']':
                    return False
                else:
                    stack.pop()
        return not stack
