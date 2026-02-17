class Solution:
    def intersection(self, nums1, nums2) :
        ans=set()
        numSet=set(nums1)
        for num in nums2:
            if num in numSet:
                ans.add(num)
        return list(ans)