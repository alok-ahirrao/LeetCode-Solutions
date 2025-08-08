class Solution:
    from functools import lru_cache

    def soupServings(self, n: int) -> float:
        if n >= 5000:
            return 1.0  # Optimization for large n

        @lru_cache(None)
        def dp(a, b):
            if a <= 0 and b <= 0:
                return 0.5  # Both empty
            if a <= 0:
                return 1.0  # A is empty first
            if b <= 0:
                return 0.0  # B is empty first

            # Probability is average of 4 choices
            return 0.25 * (
                dp(a - 4, b) +
                dp(a - 3, b - 1) +
                dp(a - 2, b - 2) +
                dp(a - 1, b - 3)
            )
        # Convert to units of 25 ml
        m = (n + 24) // 25
        return dp(m, m)