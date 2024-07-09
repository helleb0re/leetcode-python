from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()

    def dfs(path: List[int], candidates: List[int], target: int) -> List[List[int]]:

        res = []
        for i in range(len(candidates)):
            if target <= candidates[i]:
                if target == candidates[i]:
                    res.append(path + [candidates[i]])
                break

            res.extend(
                dfs(path + [candidates[i]], candidates[i:], target - candidates[i])
            )

        return res

    return dfs([], candidates, target)


if __name__ == "__main__":
    assert sorted(combinationSum([2, 3, 6, 7], 7)) == sorted([[2, 2, 3], [7]])
    assert sorted(combinationSum([2, 3, 5], 8)) == sorted(
        [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    )
    assert sorted(combinationSum([2], 1)) == sorted([])
