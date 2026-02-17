from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        count_s=Counter(s)
        sorted_items = sorted(list(count_s.items()), key=lambda x: x[1], reverse=True)
        return "".join(a[0]*a[1] for a in sorted_items)
