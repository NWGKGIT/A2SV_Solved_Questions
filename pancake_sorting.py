class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(end):
            start=0
            while start<end:
                arr[start],arr[end]=arr[end], arr[start]
                start+=1
                end-=1
        output=[]
        for i in range(len(arr)-1,-1,-1):
            curr_max_index=i
            for j in range(i):
                if arr[j]>arr[curr_max_index]:curr_max_index=j
            if curr_max_index!=i:
                flip(curr_max_index)
                flip(i)
                output.append(curr_max_index+1)
                output.append(i+1)
        return output

# MUST RETURN, AND DO AGAIN