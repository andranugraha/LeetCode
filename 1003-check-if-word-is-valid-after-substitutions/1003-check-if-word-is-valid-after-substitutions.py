class Solution:
    def isValid(self, s: str) -> bool:
        removed = True
        while removed:
            st = s.replace("abc", "")
            removed = st != s
            s = st
        
        return s == ""
        
        