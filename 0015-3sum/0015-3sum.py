class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while  left < right:
                total = nums[left] + nums[i] + nums[right]
                if total == 0:
                    result.append([nums[i],nums[left] ,nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
                       
                        
        return result


        '''
        [-4,-1,-1,0,1,2,]
        for i in this no 
        i have two pointers that starts with both 
            -left = 0
            -right = len(nums) - 1
            we go though the loop find the sum if we find thos no we can putt it in the list and append to the ans the condition stops wehn the right < left 
            - what happen if the pointers pass the currnt num index at that if we got there we should continue with out adding that index continue 
            if right or left == i :

                continue 
        '''
        