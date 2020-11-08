class Combination_40:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.helper(sorted(candidates), res, [], 0, len(candidates), target)
        return res
    
    def helper(self, candidates: List[int], res: List[List[int]], tmp: List[int], start: int, n: int, target: int):
        if target == 0:
            res.append(copy.deepcopy(tmp))
        elif target < 0:
            return
        else:
            for i in range(start, n):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                tmp.append(candidates[i])
                self.helper(candidates, res, tmp, i + 1, n, target - candidates[i])
                tmp.pop()