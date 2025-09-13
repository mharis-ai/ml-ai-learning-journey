class Solution:
    def rotate(self, nums, k: int) -> None:
        n = len(nums)
        k = k % n
        self.reverse(nums,n-k,n-1)
        self.reverse(nums,0,n-k-1)
        self.reverse(nums,0,n-1)
    def reverse(self,nums,left,right):
        while left<right:
            nums[left],nums[right] = nums[right],nums[left]
            left+=1
            right-=1