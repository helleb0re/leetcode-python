from typing import List


# iteration
def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()

    result = []

    buffer = []

    def modify_buffer(curr_sum, curr_path, curr_idx):
        for i in range(curr_idx, len(candidates)):
            # we don't need to check duplicate solutions
            if i > curr_idx and candidates[i] == candidates[i - 1]:
                continue
            # condition for finishing current path
            # if this condition is true then need to check clarifying condition
            if candidates[i] + curr_sum >= target:
                # if this solution is true then need to add (curr_path + cand[i]) to result array
                if candidates[i] + curr_sum == target:
                    result.append(curr_path + [candidates[i]])
                # we don't need to add (curr_path + cand[i]) to buffer, because
                # sum of this path will definitely be more then target
                continue

            buffer.append(
                (curr_sum + candidates[i], curr_path + [candidates[i]], i + 1)
            )

    modify_buffer(0, [], 0)

    while buffer:
        modify_buffer(*buffer.pop())

    return result


# recursion
def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()

    result = []

    def inner(curr_sum, curr_path, curr_idx):
        for i in range(curr_idx, len(candidates)):
            # we don't need to check duplicate solutions
            if i > curr_idx and candidates[i] == candidates[i - 1]:
                continue
            # condition for finishing current path
            # if this condition is true then need to check clarifying condition
            if candidates[i] + curr_sum >= target:
                # if this solution is true then need to add (curr_path + cand[i]) to result array
                if candidates[i] + curr_sum == target:
                    result.append(curr_path + [candidates[i]])
                # we don't need to add (curr_path + cand[i]) to buffer, because
                # sum of this path will definitely be more then target
                continue

            inner(curr_sum + candidates[i], curr_path + [candidates[i]], i + 1)

    inner(0, [], 0)
    return result


if __name__ == "__main__":
    assert sorted(combinationSum2([1, 2, 2, 5], 9)) == sorted([[2, 2, 5]])
    assert sorted(combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)) == sorted(
        [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    )
    assert sorted(combinationSum2([2, 5, 2, 1, 2], 5)) == sorted([[1, 2, 2], [5]])
