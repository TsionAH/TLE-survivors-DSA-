class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        
        res = [[1]]
        for i in range(1,rowIndex+1):
            each_row = [1]
            for j in range(1,i):
                each_row.append(res[i-1][j-1]+res[i-1][j])
            each_row.append(1)
            res.append(each_row)
        return res[rowIndex]