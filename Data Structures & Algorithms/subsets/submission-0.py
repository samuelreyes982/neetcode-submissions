from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []

        def dfs(i: int, path: List[int]) -> None:
            # At index i, 'path' is the subset built so far
            if i == len(nums):
                res.append(path)     # path is already a complete subset
                return

            # Choice 1: include nums[i]  -> pass a NEW list
            dfs(i + 1, path + [nums[i]])

            # Choice 2: exclude nums[i]  -> pass the SAME path (no change)
            dfs(i + 1, path)

        dfs(0, [])
        return res