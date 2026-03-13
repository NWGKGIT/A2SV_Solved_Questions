class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        k = len(s1)
        l = 0
        countS1 = Counter(s1)
        window_count = Counter(s2[l:k])
        if window_count == countS1:
            return True
        for r in range(k, len(s2)):
            window_count[s2[r]] += 1
            window_count[s2[l]] -= 1
            if window_count[s2[l]] == 0:
                del window_count[s2[l]]
            l += 1
            if window_count == countS1:
                return True
        return False
