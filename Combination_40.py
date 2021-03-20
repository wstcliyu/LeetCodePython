"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.


Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""

class Combination_40:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.helper(sorted(candidates), res, [], 0, target)
        return res
    
    def helper(self, candidates: List[int], res: List[List[int]], tmp: List[int], start: int, target: int):
        if target == 0:
            res.append(copy.deepcopy(tmp))
        else:
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                tmp.append(candidates[i])
                self.helper(candidates, res, tmp, i + 1, target - candidates[i])
                tmp.pop()
