"""
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

示例 1：
输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]

示例 2：
输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]

进阶：
请你设计时间复杂度为 O(n) 的算法解决本问题
"""

from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for j in range(n):
            if nums[j] >= 0:
                break
        new_nums = []
        i = j - 1
        while i >= 0 or j < n:
            if i == -1:
                new_nums.append(nums[j] ** 2)
                j += 1
            elif j == n:
                new_nums.append(nums[i] ** 2)
                i -= 1
            elif nums[i] ** 2 < nums[j] ** 2:
                new_nums.append(nums[i] ** 2)
                i -= 1
            else:
                new_nums.append(nums[j] ** 2)
                j += 1
        return new_nums
        # return sorted(num * num for num in nums)


print(Solution().sortedSquares([-4,-1,0,3,10]))