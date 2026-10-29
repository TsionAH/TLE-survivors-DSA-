class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in s:
            if i != ']':
                stack.append(i)
            else:
                # Collect the substring inside the brackets
                st = ''
                while stack and stack[-1] != '[':
                    st = stack.pop() + st

                # Remove the opening bracket '['
                stack.pop()

                # Collect the full repetition count
                count = ''
                while stack and stack[-1].isdigit():
                    count = stack.pop() + count

                # Repeat the substring
                st = int(count) * st

                # Push the decoded string back onto the stack
                for char in st:
                    stack.append(char)

        return ''.join(stack)