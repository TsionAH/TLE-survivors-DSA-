
class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        tr = []
        for col in range(len(matrix[0])):
            new = []
            for row in range(len(matrix)):
                new.append(matrix[row][col])
            tr.append(new)
        return tr