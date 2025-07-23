class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x > y:
            return self.getMax(s, 'a', 'b', x, y)
        else:
            return self.getMax(s, 'b', 'a', y, x)
        
    def getMax(self, s: str, a:str, b:str, x: int, y: int):
        c1 = c2 = ans = 0
        s += 'c'
        for c in s:
            if c == a:
                c1 += 1
            elif c == b:
                if c1 == 0:
                    c2 += 1
                else:
                    ans += x
                    c1 -= 1
            else:
                ans += y * min(c1, c2)
                c1 = c2 = 0
        return ans