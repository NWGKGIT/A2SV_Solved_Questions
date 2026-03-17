class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums=list(range(1,n+1))
        index=0
        while len(nums)>1:
            index=(k+index-1)%len(nums)
            nums.pop(index)
        return nums[0]