class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        z=0
        if n==0:
            return False
        if n==1:
            return True
        if n%4==0:
            z=n//4
            if z==1:
                return True
            return self.isPowerOfFour(z)
        return False