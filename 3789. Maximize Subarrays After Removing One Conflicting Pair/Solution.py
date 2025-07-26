class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        n += 1
        conflictingPairs.sort(key=lambda p: max(*p))
        conflictingPairs.append([n, n])
        max_diff = 0
        max_left = 0
        rem = 0
        max_altleft = 0
        altrem = 0
        for l, r in conflictingPairs:
            if l > r:
                l,r=r,l
            if l > max_left:
                max_diff = max(
                    max_diff, (max_altleft - max_left) * (n - r) + rem - altrem
                )
                altrem = rem
                max_altleft = max_left
                rem += (l - max_left) * (n - r)
                max_left = l
            elif l > max_altleft:
                altrem += (l - max_altleft) * (n - r)
                max_altleft = l
        return (n - 1) * n // 2 - rem + max_diff