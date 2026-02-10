def findDuplicates(nums):
    dups=[]
    for i, v in enumerate(nums):
        if nums[abs(v)-1]<=0:
            dups.append(abs(nums[i]))
        else:
            nums[abs(v)-1]*=-1
    return dups
