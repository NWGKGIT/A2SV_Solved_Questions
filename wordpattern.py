class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_to_p={}
        p_to_s={}
        slist=s.split(" ")
        if len(pattern)!=len(slist):
            return False
        for i in range(len(pattern)):
            p=pattern[i]
            char=slist[i]
            if char in s_to_p:
                if s_to_p[char]!=p:
                    return False
            else:
                s_to_p[char]=p
            
            if p in p_to_s:
                if p_to_s[p]!=char:
                    return False
            else:
                p_to_s[p]=char

        return True