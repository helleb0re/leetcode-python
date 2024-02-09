# with sorting
def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


# with hash table
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_store_symbols = {}
    t_store_symbols = {}
    for i in range(len(s)):
        s_store_symbols[s[i]] = s_store_symbols.get(s[i], 0) + 1
        t_store_symbols[t[i]] = t_store_symbols.get(t[i], 0) + 1

    return s_store_symbols == t_store_symbols


if __name__ == "__main__":
    assert isAnagram("anagram", "nagaram")
    assert not isAnagram("rat", "car")
