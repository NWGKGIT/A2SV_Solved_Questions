class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        stack=[]
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1]<temp:
                idx,tv=stack.pop()
                ans[idx]=i-idx
            stack.append((i,temp))
        return ans