# my solution (thanks for comments below the task description)
def characterReplacement(s: str, k: int) -> int:
    store = {s[0]: 1}
    max_freq_c = s[0]
    res = 1

    l = 0
    for r in range(1, len(s)):
        store[s[r]] = store.get(s[r], 0) + 1

        if store[s[r]] > store[max_freq_c]:
            max_freq_c = s[r]

        if r - l + 1 - store[max_freq_c] <= k:
            res += 1
        else:
            store[s[l]] -= 1
            l += 1

    return res


# neetcode solution
def characterReplacement(s: str, k: int) -> int:
    store = {}
    max_freq = 0
    res = 0

    l = 0
    for r in range(len(s)):
        store[s[r]] = store.get(s[r], 0) + 1

        max_freq = max(max_freq, store[s[r]])

        if r - l + 1 - max_freq <= k:
            res += 1
        else:
            store[s[l]] -= 1
            l += 1

    return res


if __name__ == "__main__":
    assert characterReplacement("ABAB", 2) == 4
    assert characterReplacement("AABABBA", 1) == 4
    assert characterReplacement("AAAB", 0) == 3
    assert characterReplacement("ABBB", 2) == 4
    assert characterReplacement("ABAA", 0) == 2
