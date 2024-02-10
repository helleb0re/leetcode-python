from typing import List


# O(n * m * logm) solution with sort
# n - len(strs); m - avg(len(strs[i]))
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    store = {}
    for s in strs:
        s_sorted = tuple(sorted(s))
        store.setdefault(s_sorted, []).append(s)

    return store.values()


# O(n * m * 26) solution with HashMap
# n - len(strs); m - avg(len(strs[i]))
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    store = {}
    for s in strs:
        key = [0] * 26  # number of lower case characters a-z
        for c in s:
            key[ord(c) - ord("a")] += 1
        store.setdefault(tuple(key), []).append(s)

    return store.values()


if __name__ == "__main__":
    assert groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ["bat"],
        ["nat", "tan"],
        ["ate", "eat", "tea"],
    ]
    assert groupAnagrams([""]) == [[""]]
    assert groupAnagrams(["a"]) == [["a"]]
