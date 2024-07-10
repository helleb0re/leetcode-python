from typing import List


# recursion
def permute(nums: List[int]) -> List[List[int]]:
    res = []

    def inner(path: List[int], nums: List[int]):
        if not nums:
            nonlocal res
            res.append(path)

        for i in range(len(nums)):
            # throw away num which we include into the path
            # nums[:i] + nums[i + 1 :] python syntax sugar
            inner(path + [nums[i]], nums[:i] + nums[i + 1 :])

    inner([], nums)
    return res


# iteration
def permute(nums: List[int]) -> List[List[int]]:
    res = []

    # current_path, current_nums
    buffer = [([], nums)]
    while buffer:
        path, curr_nums = buffer.pop()

        if not curr_nums and len(path) == len(nums):
            res.append(path)
            continue

        for i in range(len(curr_nums)):
            buffer.append((path + [curr_nums[i]], curr_nums[:i] + curr_nums[i + 1 :]))

    return res


if __name__ == "__main__":
    assert sorted(permute([1, 2, 3])) == sorted(
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    )
    assert sorted(permute([0, 1])) == sorted([[0, 1], [1, 0]])
    assert permute([1]) == [[1]]
