from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Time Complexity: O(2^n) in worst case due to subset exploration
        # Space Complexity: O(n) recursion stack + output space

        res = []
        candidates.sort()  # Sort candidates for pruning

        def backtrack(start, path, remain):
            # Base case: if remain is 0, add a copy of path to results
            if remain == 0:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):
                # Skip duplicates (if candidates[i] == candidates[i - 1])
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Prune search if current candidate exceeds remaining target
                if candidates[i] > remain:
                    break

                # Choose candidates[i] and explore further
                path.append(candidates[i])
                backtrack(i + 1, path, remain - candidates[i])
                path.pop()  # Backtrack

        backtrack(0, [], target)
        return res
