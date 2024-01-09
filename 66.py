class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = ''
        for i in range(len(digits)):
            nums+=str(digits[i])
        nums = int(nums)
        nums+=1
        nums = str(nums)
        answer = []
        for j in range(len(nums)):
            answer.append(int(nums[j]))
        return answer