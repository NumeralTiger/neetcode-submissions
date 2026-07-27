class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            charleft = s[i]
            charright = s[j]
            if not charleft.isalnum():
                i += 1
                continue
            if not charright.isalnum():
                j -= 1
                continue
            if charleft.lower() != charright.lower():
                return False
            i += 1
            j -= 1
        return True