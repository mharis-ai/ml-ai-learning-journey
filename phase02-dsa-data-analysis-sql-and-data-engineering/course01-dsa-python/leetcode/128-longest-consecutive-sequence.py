class Solution:
    def longestConsecutive(self, nums) -> int:
        if not nums:
            return 0
        
        collection = set()
        max_count = 0

        for item in nums:
            collection.add(item)

        for item in collection:
            if item - 1 in collection:
                continue
            
            count = 1
            current = item
            while current + 1 in collection:
                count += 1
                current += 1

            if count > max_count:
                max_count = count
                
        return max_count