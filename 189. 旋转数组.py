"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]

进阶：
尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？

"""
from typing import List


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        c = gcd(n, k)

        if k == 0:
            return

        for j in range(c):
            temp = nums[j]
            idx = j
            for i in range(n//c):
                new_idx = (idx + k) % n
                new_temp = nums[new_idx]
                nums[new_idx] = temp

                temp = new_temp
                idx = new_idx


nums = [1,2,3,4,5,6]
Solution().rotate(nums, 4)
print(nums)