class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=nums[0]
        currentsum=0
        for i in range(len(nums)):
            currentsum=max(nums[i], currentsum+nums[i])

            maxsum=max(currentsum,maxsum)
        return maxsum