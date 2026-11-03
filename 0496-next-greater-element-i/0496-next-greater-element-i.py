class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = {}
        stack = []
        value = []
        for i in nums2:
            while stack and i > stack[-1]:
                ans = stack.pop()
                result[ans] = i
            stack.append(i)
        for j in nums1:
            if j in result:
                value.append(result[j])
            else:
                value.append(-1)
        return value