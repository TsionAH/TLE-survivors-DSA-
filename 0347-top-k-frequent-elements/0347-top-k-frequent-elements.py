class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        res = []
        my_map = {}
        for i in nums:
            my_map[i] = my_map.get(i,0) + 1
        sore = dict(sorted(my_map.items(), key=lambda x: x[1], reverse=True))
        count = 0
        for i in sore:
            if count < k:
                res.append(i)
                count += 1

            
            
        return res