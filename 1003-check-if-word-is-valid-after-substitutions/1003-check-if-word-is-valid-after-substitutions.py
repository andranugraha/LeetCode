class Solution:
    def isValid(self, s: str) -> bool:
        state = s
        while len(s) != 0:
            s = s.replace('abc', '')
            if state != s:
                state = s
            else:
                break
        return len(s) == 0
        
        