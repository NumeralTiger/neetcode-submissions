class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=s.lower()
        t=t.lower()

        if len(s) != len(t):
            return False
        
        count = [0] * 26

        for c in s:
            count[ord(c)-ord('a')]+=1
        for c in t:
            count[ord(c)-ord('a')]-=1
        
        return [0]*26 == count