from typing import List


# my solution: O(m + n)
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    nums = []

    n1, n2 = len(nums1), len(nums2)
    k1, k2 = 0, 0

    while k1 < n1 and k2 < n2:
        if nums1[k1] < nums2[k2]:
            nums.append(nums1[k1])
            k1 += 1
        else:
            nums.append(nums2[k2])
            k2 += 1

    if k1 < n1:
        nums.extend(nums1[k1:])

    if k2 < n2:
        nums.extend(nums2[k2:])

    res = nums[(n1 + n2) // 2]
    if (n1 + n2) % 2 == 0:
        res = (res + nums[(n1 + n2) // 2 - 1]) / 2

    return res


# neetcode solution: O(log(n + m))
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    A, B = nums1, nums2
    na, nb = len(nums1), len(nums2)
    if nb < na:
        A, B = B, A
        na, nb = nb, na

    n = na + nb
    half = n // 2

    l, r = 0, na - 1
    while True:
        ma = (l + r) // 2
        mb = half - ma - 2

        Aleft = A[ma] if ma >= 0 else float("-infinity")
        Aright = A[ma + 1] if (ma + 1) < na else float("infinity")
        Bleft = B[mb] if mb >= 0 else float("-infinity")
        Bright = B[mb + 1] if (mb + 1) < nb else float("infinity")

        if Aleft <= Bright and Bleft <= Aright:
            # odd
            if n % 2:
                return min(Aright, Bright)
            # even
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:
            r = ma - 1
        else:
            l = ma + 1


if __name__ == "__main__":
    print(findMedianSortedArrays([1, 3], [2]))
    print(findMedianSortedArrays([1, 2], [3, 4]))
