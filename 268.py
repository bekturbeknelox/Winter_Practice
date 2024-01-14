class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set()
        for i in nums:
            num_set.add(i)
        n = 0
        for j in range(len(nums)+1):
            if j not in num_set:
                n += j
        return n