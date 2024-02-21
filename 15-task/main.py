from typing import List


# my first solution
def threeSum(nums: List[int]) -> List[List[int]]:
    sorted_nums = sorted(nums)

    res = []
    explored = set()
    for i in range(len(sorted_nums)):
        target = sorted_nums[i] * -1
        l, r = i + 1, len(sorted_nums) - 1

        while l < r:
            if target > sorted_nums[l] + sorted_nums[r]:
                l += 1
            elif target < sorted_nums[l] + sorted_nums[r]:
                r -= 1
            else:
                values = sorted_nums[i], sorted_nums[l], sorted_nums[r]
                if values not in explored:
                    explored.add(values)
                    res.append(list(values))
                l += 1

    return res


# the optimized solution
def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()

    res = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        target = nums[i] * -1
        l, r = i + 1, len(nums) - 1

        while l < r:
            if target > nums[l] + nums[r]:
                l += 1
            elif target < nums[l] + nums[r]:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1

    return res


if __name__ == "__main__":
    assert threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert threeSum([0, 1, 1]) == []
    assert threeSum([-2, 0, 1, 1, 2]) == [[-2, 0, 2], [-2, 1, 1]]
