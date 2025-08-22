class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        rows = [ row for row in grid ]
        cols = [ col for col in zip(*grid) ]
        m = len(rows)
        n = len(cols)

        minRow, maxRow = 0, m-1
        while minRow < m and 1 not in rows[minRow]: minRow += 1
        while maxRow >= 0 and 1 not in rows[maxRow]: maxRow -= 1
        
        minCol, maxCol = 0, n-1
        while minCol < n and 1 not in cols[minCol]: minCol += 1
        while maxCol >= 0 and 1 not in cols[maxCol]: maxCol -= 1

        return (maxRow - minRow + 1) * (maxCol - minCol + 1)