class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()

        def search(index, path, summ):
            if summ == target:
                results.append(path[:])
                return
            if summ > target or index >= len(candidates):
                return

            # include
            path.append(candidates[index])
            search(index + 1, path, summ + candidates[index])
            path.pop()

            # exclude: skip all duplicates
            next_index = index + 1
            while next_index < len(candidates) and candidates[next_index] == candidates[index]:
                next_index += 1

            search(next_index, path, summ)

        search(0, [], 0)
        return results



        