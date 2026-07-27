class Solution:
    def isValid(self, s: str) -> bool:
        map_closing_to_opening = {
            "}": "{",
            ")": "(",
            "]": "[",
        }
        stack = []
        for ch in s:
            if ch in map_closing_to_opening:
                if not stack or map_closing_to_opening[ch] != stack.pop():
                    return False
            else:
                stack.append(ch)
    
        return len(stack) == 0