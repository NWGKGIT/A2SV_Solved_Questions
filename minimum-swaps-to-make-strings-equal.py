class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        mismatches=Counter()
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                mismatches[(s1[i],s2[i])]+=1
        
        xy=mismatches[("x","y")]
        yx=mismatches[("y","x")]
        if (xy+yx)%2!=0:
            return -1
        swaps=0
        swaps+=xy//2
        swaps+=yx//2
        if xy %2!=0:
            swaps+=2
        return swaps