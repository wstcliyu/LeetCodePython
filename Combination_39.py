class Combiantion_39:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.helper(sorted(candidates), res, [], 0, target)
        return res
    
    def helper(self, candidates: List[int], res: List[List[int]], tmp: List[int], start: int, target: int):
        if target == 0:
            res.append(copy.deepcopy(tmp))
        else:
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    return
                tmp.append(candidates[i])
                self.helper(candidates, res, tmp, i, target - candidates[i])
                tmp.pop()
