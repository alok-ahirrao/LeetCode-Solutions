class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        crt = 0
        for i in arr:
            if i%2!=0:
                crt +=1
                if crt >=3:
                    return True
            else:
                crt = 0 
        return False 