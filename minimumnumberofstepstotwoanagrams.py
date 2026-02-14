from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s=Counter(s)
        count_t=Counter(t)
        steps=0
        for char,count in count_s.items():
            if count>count_t[char]:
                steps+=count-count_t[char]
        return steps