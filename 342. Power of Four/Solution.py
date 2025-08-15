class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<0:
            return False
        i=0
        while True:
            temp = 4**i
            if temp==n:
                return True
            elif temp>n:
                return False
            i+=1