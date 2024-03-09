from collections import deque


# my solution
def minWindow(s, t):
    dict_t = {}
    for c in t:
        dict_t[c] = dict_t.get(c, 0) + 1

    dict_s = {}
    l, r = 0, 0
    buff = deque()
    over = {}
    best = [l, r]
    for i in range(len(s)):
        curr_char = s[i]
        if curr_char in dict_t:
            buff.append(i)
            if dict_s.get(curr_char, 0) < dict_t[curr_char]:
                dict_s[curr_char] = dict_s.get(curr_char, 0) + 1
            elif dict_s.get(curr_char, 0) == dict_t[curr_char]:
                over[curr_char] = over.get(curr_char, 0) + 1

        if dict_s == dict_t:
            while s[l] not in dict_t:
                l += 1
            while s[l] in over:
                over[s[l]] -= 1
                if over[s[l]] == 0:
                    del over[s[l]]

                buff.popleft()
                l = buff[0]
                r = i
            if best[1] == 0 or best[1] - best[0] > r - l + 1:
                best = [l, r + 1]
        else:
            r += 1

    return s[best[0] : best[1]]


def minWindow(s, t):
    dict_t = {}
    for c in t:
        dict_t[c] = dict_t.get(c, 0) + 1

    window_store = {}
    best = [0, 0]
    have, need = 0, len(dict_t)
    l = 0
    for r in range(len(s)):
        curr_char = s[r]
        if curr_char in dict_t:
            window_store[curr_char] = window_store.get(curr_char, 0) + 1

            if window_store[curr_char] == dict_t[curr_char]:
                have += 1

            while have == need:
                # update result
                if best[1] == 0 or best[1] - best[0] > r - l + 1:
                    best = [l, r + 1]

                if s[l] in dict_t:
                    window_store[s[l]] -= 1
                    if window_store[s[l]] < dict_t[s[l]]:
                        have -= 1

                l += 1

    return s[best[0] : best[1]]


if __name__ == "__main__":
    assert minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert minWindow("a", "a") == "a"
    assert minWindow("a", "aa") == ""
    assert minWindow("ab", "b") == "b"
    assert minWindow("bbaac", "aba") == "baa"
