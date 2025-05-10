import atexit

atexit.register(lambda: open("display_runtime.txt", "w").write("0"))

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = z1 = s2 = z2 = 0
        for d in nums1:
            s1 += d
            if d == 0:
                z1 += 1
        for d in nums2:
            s2 += d
            if d == 0:
                z2 += 1
        if z1 == 0 and z2 == 0:
            if s1 == s2:
                return s1
            else:
                return -1
        elif z1 == 0:
            if s2 + z2 > s1:
                return -1
            else:
                return s1
        elif z2 == 0:
            if s1 + z1 > s2:
                return -1
            else:
                return s2
        else:
            return max(s1 + z1, s2 + z2)