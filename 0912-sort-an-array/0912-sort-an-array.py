class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def mergeSort(numbers):
            
            n = len(numbers)
            mid = n//2
            if len(numbers) <= 1:
                return numbers
            L = numbers[:mid]
            R = numbers[mid:]
            L = mergeSort(L)
            R = mergeSort(R)
            sorted_arr =[]
            l,r = 0,0
            while l < len(L) and r < len(R):
                if L[l] <= R[r]:
                    sorted_arr.append(L[l])
                    l += 1
                else:
                    sorted_arr.append(R[r])
                    r += 1
                
            sorted_arr.extend(L[l:])
            sorted_arr.extend(R[r:])
            return sorted_arr
        return mergeSort(nums)
