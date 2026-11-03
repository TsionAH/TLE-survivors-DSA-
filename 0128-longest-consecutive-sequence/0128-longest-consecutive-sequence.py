class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        my_nums = set(nums)
        max_count = 0

        for i in my_nums:
            if i - 1 not in my_nums:
                curr_num = i
                count = 1
                while curr_num + 1 in my_nums:
                    curr_num += 1
                    count += 1
                max_count = max(max_count,count)
        return max_count
        '''
        first identify the min form the list
        save the min
        put all the nums in the dic that way easy to find in o(1) time so it take as o(n) space complexity 
        we should initalize our counter of the conscutive from 0 
        - till not find the next conscutive we will go so if we did not find we can return the count 
        - edge case it may have other conscutive so we should check it also and compare the max and return the max for this case i have the first max so i should find the min that is greter that the max min(max,float('inf)) 
        '''