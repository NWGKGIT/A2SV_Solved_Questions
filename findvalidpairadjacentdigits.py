class Solution:
    def findValidPair(self, s: str) -> str:
        countS=Counter(s)
        for i in range(1,len(s)):
            elem, nextelem=s[i-1], s[i]
            if nextelem!= elem and countS[elem]==int(elem) and countS[nextelem]==int(nextelem):
                    return elem+nextelem

        return ""