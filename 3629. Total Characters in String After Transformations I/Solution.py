class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        count = [0] * 26
        
        # Initialize count of each character in the string
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        
        total_length = len(s)
        
        # Perform t transformations
        for _ in range(t):
            new_count = [0] * 26
            for i in range(26):
                if i == 25:  # 'z'
                    new_count[0] = (new_count[0] + count[25]) % MOD  # 'a'
                    new_count[1] = (new_count[1] + count[25]) % MOD  # 'b'
                    total_length = (total_length + count[25]) % MOD
                else:
                    new_count[i + 1] = (new_count[i + 1] + count[i]) % MOD
            count = new_count
        
        return total_length % MOD
