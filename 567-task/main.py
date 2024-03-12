# my solution O(26*n)
def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    store = {}
    for c in s1:
        store[c] = store.get(c, 0) + 1

    l = 0
    tmp_store = {}
    for r in range(len(s2)):
        c = s2[r]
        if c in store:
            tmp_store[c] = tmp_store.get(c, 0) + 1
            while tmp_store[c] > store[c]:
                tmp_store[s2[l]] -= 1
                l += 1

            if tmp_store == store:
                return True
        else:
            l = r + 1
            tmp_store.clear()

    return False

# neetcode solution O(n)
def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    # number of all lowercase English letters - 26
    store_s1 = [0] * 26
    store_s2 = [0] * 26
    for i in range(len(s1)):
        store_s1[ord(s1[i]) - ord("a")] += 1
        store_s2[ord(s2[i]) - ord("a")] += 1

    matches = 0
    for i in range(26):
        matches += 1 if store_s1[i] == store_s2[i] else 0

    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26:
            return True

        c2_l_ind = ord(s2[l]) - ord("a")
        store_s2[c2_l_ind] -= 1
        if store_s1[c2_l_ind] == store_s2[c2_l_ind]:
            matches += 1
        elif store_s1[c2_l_ind] - 1 == store_s2[c2_l_ind]:
            matches -= 1

        c2_r_ind = ord(s2[r]) - ord("a")
        store_s2[c2_r_ind] += 1
        if store_s1[c2_r_ind] == store_s2[c2_r_ind]:
            matches += 1
        elif store_s1[c2_r_ind] + 1 == store_s2[c2_r_ind]:
            matches -= 1

        l += 1

    return matches == 26


if __name__ == "__main__":
    assert checkInclusion("ab", "eidbaooo")
    assert not checkInclusion("ab", "eidboaoo")
    assert checkInclusion("adc", "dcda")
    assert checkInclusion("ad", "cdda")
    assert not checkInclusion("hello", "ooolleoooleh")
    assert checkInclusion("abc", "baxyzabc")
    assert checkInclusion("abc", "bbbca")
