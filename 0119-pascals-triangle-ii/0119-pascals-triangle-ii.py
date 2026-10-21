class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        result = [1]
        for i in range(1,rowIndex+1):
            next_element = result[i-1] *(rowIndex - i + 1)//i
            result.append(next_element)
       
        return result