class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        n = len(nums)
        a,b = 0,0
        for i in range(n):
            if nums[i] == 1:
                a+=1
                if a>b:
                    b = a
            else:
                a = 0
        return b