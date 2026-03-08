class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magwords=Counter( [ch for ch in magazine] )
        for ch in ransomNote:
            if magwords[ch]>0:
                magwords[ch]-=1
            else:
                return False
        return True