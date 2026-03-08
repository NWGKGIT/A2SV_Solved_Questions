class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        numSet=set(nums)
        _max=0
        for num in numSet:
            if num-1 not in numSet:
                    
                curr=0
                i=0
                while (num+i) in numSet:
                    curr+=1
                    i+=1
                _max=max(curr,_max)
        return _max