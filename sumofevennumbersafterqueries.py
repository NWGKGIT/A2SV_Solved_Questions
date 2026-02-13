class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        current_even_sum = 0 
        for num in nums:
            if num %2==0:
                current_even_sum+=num
        answer = []
        
        for val, idx in queries:
            old_val = nums[idx]
            if old_val % 2 == 0:
                current_even_sum -= old_val
            nums[idx] += val
            new_val = nums[idx]
            if new_val % 2 == 0:
                current_even_sum += new_val   
            answer.append(current_even_sum) 
        return answer