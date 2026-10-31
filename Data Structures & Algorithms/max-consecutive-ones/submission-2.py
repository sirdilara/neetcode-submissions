class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_val = 0
        curr = 0
        for x in nums:
            if x == 1:
                curr += 1
                max_val = max(max_val, curr)
            else:
                curr = 0
        return max_val

             

        