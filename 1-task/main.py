from typing import List


# my solution
def twoSum(nums: List[int], target: int) -> List[int]:
    hash_container = dict()
    for i in range(len(nums)):
        hash_container.setdefault(nums[i], set()).add(i)

    for i in range(len(nums)):
        search_num = target - nums[i]
        if search_num in hash_container:
            res = [e for e in hash_container[search_num]]
            if search_num != nums[i]:
                return [i] + res[:1]
            elif len(res) > 1:
                return res[:2]

    return [-1, -1]


# best solution
def twoSum(nums: List[int], target: int) -> List[int]:
    numMap = {}
    n = len(nums)

    for i in range(n):
        complement = target - nums[i]
        if complement in numMap:
            return [numMap[complement], i]
        numMap[nums[i]] = i

    return []  # No solution found

if __name__ == "__main__":
    assert twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert twoSum([3, 2, 4], 6) == [1, 2]
    assert twoSum([3, 3], 6) == [0, 1]
