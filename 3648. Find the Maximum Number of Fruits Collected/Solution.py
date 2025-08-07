class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        ans = 0
        for i in range(n):
            ans += fruits[i][i]
        dp_bottom = [fruits[n-1][0], 0, 0]
        dp_right = [fruits[0][n-1], 0, 0]
        max_reachable = 2
        for i in range(1, n-1):
            dp_bottom_new = [0]*(max_reachable+2)
            dp_right_new = [0]*(max_reachable+2)
            for j in range(max_reachable):
                dp_bottom_new[j] = max(dp_bottom[j-1], dp_bottom[j], dp_bottom[j+1])+fruits[n-1-j][i]
                dp_right_new[j] = max(dp_right[j-1], dp_right[j], dp_right[j+1])+fruits[i][n-1-j]
            dp_bottom = dp_bottom_new
            dp_right = dp_right_new
            if max_reachable-n+4+i <= 1:
                max_reachable += 1
            elif max_reachable-n+3+i > 1:
                max_reachable -= 1
        return ans+dp_right[0]+dp_bottom[0]