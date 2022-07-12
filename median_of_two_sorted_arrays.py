"""
    Given two sorted arrays nums1 and nums2 of size m and n 
    respectively, return the median of the two sorted arrays.
"""

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        arr =  sorted(nums1 + nums2)
        if len(arr) % 2 == 0:
            return (arr[len(arr)//2] + arr[len(arr)//2 - 1]) / 2
        else:
            return arr[len(arr)//2]
        