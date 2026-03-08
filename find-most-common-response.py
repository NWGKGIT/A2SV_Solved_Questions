class Solution:
    def findCommonResponse(self,responses):
        if not responses:
            return ""
        count = Counter(i for sub in responses for i in set(sub))
        
        return min(count.keys(), key=lambda k:(-count[k],k) )
        # absolute abomination that I have to use min to find max. 