class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        diff=[0]*(len(s)+1)
        for shift in shifts:
            l=shift[0]
            r=shift[1]
            v=shift[2]
            if v==0:
                diff[l]-=1
                diff[r+1]+=1
            elif v==1:
                diff[l]+=1
                diff[r+1]-=1
        accum=0
        for i in range(len(diff)):
            accum+=diff[i]
            diff[i]=accum
        slist=list(s)
        for i in range(len(slist)):
            shftidx=(ord(slist[i])-ord("a")+diff[i])%26
            slist[i]=chr(shftidx+ord("a"))

        return "".join(slist)
