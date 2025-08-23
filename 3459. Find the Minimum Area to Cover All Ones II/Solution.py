class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = rows * cols

        def compute_slice(is_horizontal):
            size = rows if is_horizontal else cols
            other_size = cols if is_horizontal else rows
            slices = [[(float('inf'), float('inf'), float('-inf'), float('-inf'))] * size for _ in range(size)]
            
            for i in range(size):
                start, end = float('inf'), float('-inf')
                for j in range(other_size):
                    val = grid[i][j] if is_horizontal else grid[j][i]
                    if val:
                        if start == float('inf'):
                            start = j
                        end = j
                
                if start == float('inf'):
                    for k in range(i):
                        slices[k][i] = slices[k][i-1]
                else:
                    slices[i][i] = (i, start, i, end) if is_horizontal else (start, i, end, i)
                    for k in range(i):
                        prev = slices[k][i-1]
                        slices[k][i] = (
                            min(prev[0], i if is_horizontal else start),
                            min(prev[1], start if is_horizontal else i),
                            i if is_horizontal else max(prev[2], end),
                            max(prev[3], end if is_horizontal else i)
                        )
            return slices

        h_slices = compute_slice(True)
        v_slices = compute_slice(False)

        def compute_corner(is_top, is_left):
            corner = [[(float('inf'), float('inf'), float('-inf'), float('-inf'))] * (cols + 1) for _ in range(rows + 1)]
            r_range = range(rows) if is_top else range(rows - 1, -1, -1)
            c_range = range(cols) if is_left else range(cols - 1, -1, -1)
            
            for r in r_range:
                for c in c_range:
                    if grid[r][c]:
                        corner[r][c] = (
                            min(r, corner[r-1][c][0], corner[r][c-1][0]) if is_top else r,
                            min(c, corner[r-1][c][1], corner[r][c-1][1]) if is_left else c,
                            r if is_top else max(r, corner[r+1][c][2], corner[r][c+1][2]),
                            c if is_left else max(c, corner[r-1][c][3], corner[r][c+1][3])
                        )
                    else:
                        prev_r = r - 1 if is_top else r + 1
                        prev_c = c - 1 if is_left else c + 1
                        corner[r][c] = (
                            min(corner[prev_r][c][0], corner[r][prev_c][0]),
                            min(corner[prev_r][c][1], corner[r][prev_c][1]),
                            max(corner[prev_r][c][2], corner[r][prev_c][2]),
                            max(corner[prev_r][c][3], corner[r][prev_c][3])
                        )
            return corner

        tl_corner = compute_corner(True, True)
        tr_corner = compute_corner(True, False)
        bl_corner = compute_corner(False, True)
        br_corner = compute_corner(False, False)

        def calculate_area(coords):
            return (coords[2] - coords[0] + 1) * (coords[3] - coords[1] + 1) if coords[0] < float('inf') else 0

        min_area = max_area

        for i in range(1, rows):
            for j in range(i + 1, rows):
                area1 = calculate_area(h_slices[0][i-1])
                area2 = calculate_area(h_slices[i][j-1])
                area3 = calculate_area(h_slices[j][rows-1])
                min_area = min(min_area, area1 + area2 + area3)

            for j in range(1, cols):
                area1 = calculate_area(h_slices[0][i-1])
                area2 = calculate_area(bl_corner[i][j-1])
                area3 = calculate_area(br_corner[i][j])
                min_area = min(min_area, area1 + area2 + area3)

                area1 = calculate_area(h_slices[i][rows-1])
                area2 = calculate_area(tl_corner[i-1][j-1])
                area3 = calculate_area(tr_corner[i-1][j])
                min_area = min(min_area, area1 + area2 + area3)

        for i in range(1, cols):
            for j in range(i + 1, cols):
                area1 = calculate_area(v_slices[0][i-1])
                area2 = calculate_area(v_slices[i][j-1])
                area3 = calculate_area(v_slices[j][cols-1])
                min_area = min(min_area, area1 + area2 + area3)

            for j in range(1, rows):
                area1 = calculate_area(v_slices[0][i-1])
                area2 = calculate_area(tr_corner[j-1][i])
                area3 = calculate_area(br_corner[j][i])
                min_area = min(min_area, area1 + area2 + area3)

                area1 = calculate_area(v_slices[i][cols-1])
                area2 = calculate_area(tl_corner[j-1][i-1])
                area3 = calculate_area(bl_corner[j][i-1])
                min_area = min(min_area, area1 + area2 + area3)

        return min_area