class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if all(num==0 for num in nums): return "0"
        numstr=list(map(str,nums))
        numstr.sort(key=lambda x:x*10, reverse=True)
        return "".join(numstr)