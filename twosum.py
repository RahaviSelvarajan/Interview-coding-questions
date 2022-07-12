"""
    Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in nums:
            copy = nums.copy()
            copy[nums.index(x)] = None
            if target-x in copy:
                arr = [nums.index(x)]   
                arr.append(copy.index(target-x))
                return arr