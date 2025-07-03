class Solution:
    def kthCharacter(self, k: int) -> str:
        # string=["a"]
        # while len(string)<=k:
        #     next_string=[chr(((ord(c)-ord('a')+1)%26)+ord('a')) for c in string]
        #     string+=next_string
        # return string[k-1]

        ans = 0
        while k != 1:
            t = k.bit_length() - 1
            if (1 << t) == k:
                t -= 1
            k -= 1 << t
            ans += 1
        return chr(ord("a") + ans)
        