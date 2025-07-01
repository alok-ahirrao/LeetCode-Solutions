class Solution:
    def possibleStringCount(self, word: str) -> int:

        stack = []
        ans = 1 
        for w in word:
            if not stack or (stack and w==stack[-1]):
                stack.append(w)
            else:
                ans+=len(stack)-1
                stack = [w]
            
            #print(w,stack,ans)

        ans+=len(stack)-1
        return ans 

        