import operator
from functools import reduce

class Solution:
    def singleNumber(self, nums):
        result = reduce(operator.xor, nums)
        return result
