class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        
        changed.sort()
        frequency_counter = Counter(changed)
        original = []
        
        for num in changed:
            if frequency_counter[num] == 0:
                continue
            
            frequency_counter[num] -= 1
            
            if frequency_counter[num * 2] > 0:
                frequency_counter[num * 2] -= 1
                original.append(num)
            else:
                return []
                
        return original