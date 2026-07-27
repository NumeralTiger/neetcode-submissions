class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        i , j = 0 , len(s) - 1
        while i < j:
            charleft = s[i]
            charright = s[j]
            if charleft.isalnum() and charright.isalnum():
                if charleft.lower() != charright.lower():
                    return False
                i += 1
                j -= 1
                continue
            if not charleft.isalpha():
                i += 1
            if not charright.isalpha():
                j -= 1
        return True
            