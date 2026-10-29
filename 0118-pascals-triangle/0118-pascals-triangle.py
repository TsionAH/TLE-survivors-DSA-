class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        
        rows = [[1]]
        
        for i in range(1,numRows):
            each_row = [1]
            for j in range(1,i):
                
                each_row.append(rows[i-1][j-1]+rows[i-1][j])
            each_row.append(1)  
            rows.append(each_row)
        return rows



