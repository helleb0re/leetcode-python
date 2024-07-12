from typing import List


# my explanation
# result: [[]]
## result: [[], [1]]
### result: [[], [1], [2], [1, 2]]
#### result: [ |[], [1],| [2], [1, 2], [1, 2, 2], [2, 2]]
####           ----------   --> we skipped these elements, because we have already concatenated them
####                            with prev elem which equal to curr elem


def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    nums.sort()

    result = [[]]
    prev_result_len = 0
    for i in range(len(nums)):
        curr_result_len = len(result)
        start = 0

        if i > 0 and nums[i - 1] == nums[i]:
            start = prev_result_len

        for j in range(start, curr_result_len):
            result.append(result[j] + [nums[i]])

        prev_result_len = curr_result_len

    return result


# recursive (dfs) (neetcode explanation)
def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    nums.sort()

    result = []

    def inner(path, k):
        if k == len(nums):
            nonlocal result
            result.append(path)
            return

        inner(path + [nums[k]], k + 1)
        while k + 1 != len(nums) and nums[k] == nums[k + 1]:
            k += 1
        inner(path, k + 1)
        return

    inner([], 0)

    return result


# iterative (bfs) (neetcode explanation)
def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    nums.sort()

    result = []
    buffer = [([], 0)]
    while buffer:
        path, curr_idx = buffer.pop()

        if curr_idx == len(nums):
            result.append(path)
            continue

        buffer.append((path + [nums[curr_idx]], curr_idx + 1))
        while curr_idx + 1 != len(nums) and nums[curr_idx] == nums[curr_idx + 1]:
            curr_idx += 1
        buffer.append((path, curr_idx + 1))

    return result


if __name__ == "__main__":
    assert sorted(subsetsWithDup([1, 2, 2])) == sorted(
        [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    )
    assert sorted(subsetsWithDup([0])) == sorted([[], [0]])
