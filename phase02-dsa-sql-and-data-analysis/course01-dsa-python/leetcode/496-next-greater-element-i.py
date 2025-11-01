class Solution:
    def nextGreaterElement(self, nums1, nums2):
        n = len(nums2)
        stack = []
        result = {}
        
        for i in range(n-1, -1, -1):
            while stack and nums2[i] >= stack[-1]:
                stack.pop()
            if stack:
                result[nums2[i]] = stack[-1]
            else:
                result[nums2[i]] = -1
                
            stack.append(nums2[i])
        
        return [result[i] for i in nums1]