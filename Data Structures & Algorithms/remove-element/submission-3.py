"""
Problem: Remove Element
Link: https://neetcode.io/problems/remove-element/question
Category: Array / Two Pointers

Approach:
Use a write pointer (`k`) to track the position where the next element not equal
to `val` should be placed. Iterate through the array with a read pointer (`i`).
Whenever `nums[i]` is not equal to `val`, copy it to `nums[k]` and increment `k`.
Elements equal to `val` are skipped. After the iteration, the first `k` elements
contain all values that should remain, so return `k`.

The order of the remaining elements is preserved, although the problem does not
require preserving order.

Time Complexity: O(n) - We traverse the array once.
Space Complexity: O(1) - Only constant extra space is used.
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1   
        return k

        