def containsDuplicate(nums: list[int]) -> bool:
    unique_nums = set()
    for num in nums:
        if num in unique_nums:
            return True
        unique_nums.add(num)
    return False

if __name__ == '__main__':
    assert containsDuplicate([1,1,1,3,3,4,3,2,4,2])
    assert containsDuplicate([1,2,3,1])
    assert not containsDuplicate([1,2,3,4])