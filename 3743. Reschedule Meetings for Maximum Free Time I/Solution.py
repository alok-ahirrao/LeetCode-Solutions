class Solution:
    def maxFreeTime(self, t: int, k: int, s: List[int], e: List[int]) -> int:
        q = [*map(sub,s+[t],[0]+e)]
        return max(accumulate(map(sub,q[k+1:],q),lambda p,w:p+w,initial=sum(q[:k+1])))
        return max(accumulate(zip(q[k+1:],q),lambda p,w:p+w[0]-w[1],initial=sum(q[:k+1])))
        return max(accumulate(range(k+1,len(q)),lambda p,i:p+q[i]-q[i-k-1],initial=sum(q[:k+1])))