class Solution:
    def romanToInt(self, s: str) -> int:
        hash={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        sum=hash[s[0]]
        for i in range(1,len(s)):
            if hash[s[i-1]]<hash[s[i]]:
                sum+=hash[s[i]]-2*hash[s[i-1]]
            else:
                sum+=hash[s[i]]
        return sum