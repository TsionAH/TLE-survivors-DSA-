class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        
        out_put = []
        result = []
        for i in range(len(nums1)- 1, -1, -1):
            max_stack = []
            n = nums2.copy()
            for j in range(len(nums2)- 1, -1, -1):
                if nums1[i] < nums2[j]:
                    max_stack.append(n.pop())
                elif nums1[i] == nums2[j]:
                    if max_stack:
                        out_put.append(max_stack[-1])
                        break
                    else:
                        out_put.append(-1)
                else:
                    n.pop()
        
        for k in range(len(out_put)):
            val = out_put.pop()
            result.append(val)
        return result




