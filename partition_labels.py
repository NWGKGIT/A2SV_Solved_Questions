class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        s_to_i={}
        for i,ch in enumerate(s):
            s_to_i[ch]=i
        end=0
        res=[]
        l=0
        for i,ch in enumerate(s):
            curr=s_to_i[ch]
            if curr>end:
                end=curr
            if i==end:
                res.append(i-l+1)
                l=end+1
        return res
