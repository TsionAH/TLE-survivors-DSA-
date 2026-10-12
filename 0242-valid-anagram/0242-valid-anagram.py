class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort_s = sorted(s)
        # sort_t = sorted(t)
        # if sort_s == sort_t:
        #     return True
        # return False
        my_dict = {}
        my_dict2 = {}
        for i in s:
            my_dict[i] = my_dict.get(i, 0) + 1
        for i in t:
            my_dict2[i] = my_dict2.get(i,0) + 1
        for i in my_dict:
            if my_dict2.get(i,0) != my_dict[i]:
                return False
        if len(my_dict2) != len(my_dict):
            return False
        return True
