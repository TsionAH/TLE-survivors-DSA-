class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        # result = []
        # def isAnagram(n :str , p:str) -> bool:
        #     my_dict = {}
        #     my_dict2 = {}
        #     for i in n:
        #         my_dict[i] = my_dict.get(i, 0) + 1
        #     for i in p:
        #         my_dict2[i] = my_dict2.get(i,0) + 1
        #     for i in my_dict:
        #         if my_dict2.get(i,0) != my_dict[i]:
        #             return False
        #     if len(my_dict2) != len(my_dict):
        #         return False
        #     return True
        # length_p = len(p)
        # length_s = len(s)
        # for i in range(length_s):
        #     sliding = s[i:i+length_p]
        #     if isAnagram(sliding,p):
        #         result.append(i)
        # return result 
        

        result = []

        length_p = len(p)
        length_s = len(s)

        if length_p > length_s:
            return result

        my_dict = {}
        my_dict2 = {}

        # Count characters in p and the first window of s
        for i in range(length_p):
            my_dict[p[i]] = my_dict.get(p[i], 0) + 1
            my_dict2[s[i]] = my_dict2.get(s[i], 0) + 1

        if my_dict == my_dict2:
            result.append(0)

        # Slide the window
        for i in range(length_p, length_s):
            # Remove the character leaving the window
            left_char = s[i - length_p]
            my_dict2[left_char] -= 1

            if my_dict2[left_char] == 0:
                del my_dict2[left_char]

            # Add the character entering the window
            my_dict2[s[i]] = my_dict2.get(s[i], 0) + 1

            if my_dict == my_dict2:
                result.append(i - length_p + 1)

        return result

