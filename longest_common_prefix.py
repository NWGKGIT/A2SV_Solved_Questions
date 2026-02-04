class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        first=strs[0]
        last=strs[-1]
        prefix=""
        for i in range(min(len(first),len(last))):
            if first[i] != last[i]:
                return prefix
            prefix+=last[i]
        return prefix