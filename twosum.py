class Solution(object):
    def twoSum(self, nums, target):
        hash={}
        for i in range(len(nums)):
            difference = target-nums[i]
            if nums[i] in hash:
                return [i,hash[nums[i]]]
            hash[difference]=i


