class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        rows = grid
        columns = []

        column = []
        for i in range(len(grid)):
            for j in grid:
                column.append(j[i])
            columns.append(column)
            column = []

        count = 0

        for row in rows:
            for column in columns:
                if row == column:
                    count += 1

        return count