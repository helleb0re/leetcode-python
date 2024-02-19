def isPalindrome(s: str) -> bool:
    p1, p2 = 0, len(s) - 1
    while p1 < p2:
        c1 = s[p1].lower()
        if not c1.isalnum():
            p1 += 1
            continue

        c2 = s[p2].lower()
        if not c2.isalnum():
            p2 -= 1
            continue

        if c1 != c2:
            return False

        p1, p2 = p1 + 1, p2 - 1

    return True


if __name__ == "__main__":
    assert isPalindrome("A man, a plan, a canal: Panama")
    assert not isPalindrome("race a car")
    assert isPalindrome("aa")
