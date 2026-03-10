class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash=defaultdict(lambda: -1)
        stack=[]
        for num in nums2:
            while stack and stack[-1]<num:
                hash[stack[-1]]=num
                stack.pop()
            stack.append(num)

        return [hash[num] for num in nums1]