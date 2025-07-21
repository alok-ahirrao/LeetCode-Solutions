class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        
        prev = s[0]
        answer = []
        answer.append(s[0])
        flag = False
        for c in s[1:]:
            if prev != c:
                prev = c
                answer.append(c)
                flag = False
                continue
            if flag is False:
                answer.append(c)
                flag = True
        return "".join(answer)

            
        