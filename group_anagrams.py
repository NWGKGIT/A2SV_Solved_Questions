from collections import defaultdict
from collections import Counter

class Solution:
    def groupAnagrams(self, strs):
        freq = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord("a")] += 1
            freq[tuple(count)].append(s)
        return [*freq.values()]
