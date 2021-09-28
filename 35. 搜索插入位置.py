from typing import List
"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。
示例 1:

输入: nums = [1,3,5,6], target = 5
输出: 2
示例2:

输入: nums = [1,3,5,6], target = 2
输出: 1
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > target:
                left = mid + 1
            elif nums[mid] < target:
                right = mid - 1
            else:
                return mid

        return left
