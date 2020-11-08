class Combiantion_39:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.helper(candidates, res, [], 0, len(candidates), target)
        return res
    
    def helper(self, candidates: List[int], res: List[List[int]], tmp: List[int], start: int, n: int, target: int):
        if target == 0:
            res.append(copy.deepcopy(tmp))
        elif target < 0:
            return
        else:
            for i in range(start, n):
                tmp.append(candidates[i])
                self.helper(candidates, res, tmp, i, n, target - candidates[i])
                tmp.pop()
        