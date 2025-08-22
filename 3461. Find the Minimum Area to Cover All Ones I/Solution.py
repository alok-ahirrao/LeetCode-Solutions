class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        l=[0,0]
        b=[float('inf'),0]
        f1=True
        for i in range(len(grid)):
            if 1 in grid[i]:
                if f1:
                    l[0]=i
                    f1=False
                l[1]=i
            else:
                continue
            c=grid[i][::-1]
            b[0]=min(b[0],grid[i].index(1))
            b[1]=max(b[1],len(grid[i])-c.index(1))
        l=l[1]-l[0]+1
        b=b[1]-b[0]
        return l*b