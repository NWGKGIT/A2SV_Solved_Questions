class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        total_len = len(nums)
        total_bothdom_count = nums.count(candidate)
        if total_bothdom_count <= total_len/2:
            return -1
        

        left_count = 0
        for i in range(total_len - 1): 
            if nums[i] == candidate:
                left_count += 1
            right_count=total_bothdom_count-left_count
            
            if right_count==left_count:
                return i
            
                
        return -1