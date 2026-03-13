class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l=0
        r=len(people)-1
        boats=0
        while l<=r:
            sum_of_ends=people[l]+people[r]
            if sum_of_ends<=limit:
                l+=1
            r-=1
            boats+=1
        return boats
