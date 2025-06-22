class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        if len(s)%k!=0: # checking if we can divide string into k parts
            for i in range (k-(len(s)%k)): # if we can't divide fill the remaining required part
                s+=fill
        i=0
        l=[] # taking list to append parts of s
        while i<len(s):
            l.append(s[i:i+k]) # taking parts of string of size k
            i+=k 
        return l # return the list 