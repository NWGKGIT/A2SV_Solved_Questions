def separateDigits(nums):
    res=[]
    for num in nums:
        for digit in str(num):
            res.append(int(digit))
    return res
