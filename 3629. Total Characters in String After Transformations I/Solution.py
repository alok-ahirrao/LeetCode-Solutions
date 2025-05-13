from collections import Counter

MOD = 10**9 + 7
MAX_T = 100_000

# Precompute length growth for each possible (char + t)
dp = [1] * (MAX_T + 26)
for i in range(26, len(dp)):
    dp[i] = (dp[i - 26] + dp[i - 25]) % MOD

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        cnt = Counter(s)
        ans = 0
        for ch, freq in cnt.items():
            index = (ord(ch) - ord('a')) + t
            ans = (ans + freq * dp[index]) % MOD
        return ans
