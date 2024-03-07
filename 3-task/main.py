from itertools import islice


# my solution
def lengthOfLongestSubstring(s: str) -> int:
    store = {}

    best = start = end = 0
    for i, c in enumerate(s):
        if c in store:
            best = max(best, end - start)
            start = store[c] + 1
            # remove values until key != curr_char
            for key in list(store.keys()):
                del store[key]
                if key == c:
                    break

        store[c] = i
        end += 1

    return max(best, end - start)


# neetcode solution
def lengthOfLongestSubstring(s: str) -> int:
    store = set()
    res = start = 0
    for i, c in enumerate(s):
        while c in store:
            store.remove(s[start])
            start += 1

        store.add(c)
        res = max(res, i - start + 1)

    return res


if __name__ == "__main__":
    assert lengthOfLongestSubstring("abcabcbb") == 3
    assert lengthOfLongestSubstring("bbbbb") == 1
    assert lengthOfLongestSubstring("pwwkew") == 3
