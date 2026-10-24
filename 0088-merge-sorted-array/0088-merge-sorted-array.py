class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = 0
        right = 0
        while left < m and nums2 and nums1:
            if nums1[left] <= nums2[right]:
                left += 1
            else:
                temp = nums1[left]
                nums1[left] = nums2[right]
                nums2[right] = temp
                nums2.sort()
        index = 0
        for i in range(m,len(nums1)):
            nums1[i] = nums2[index]
            index += 1