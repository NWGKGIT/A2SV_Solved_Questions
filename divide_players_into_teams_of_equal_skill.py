class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l=0
        r=len(skill)-1
        pairings=[]
        expected_sum=skill[l]+skill[r]
        result=0
        while l<=r:
            if skill[l]+skill[r]==expected_sum:
                pairings.append((skill[l],skill[r]))
                result+=skill[l]*skill[r]
            else:
                return -1
            l+=1
            r-=1
        return result

# not the most optimal (could be made o(n))