def isValid(s: str) -> bool:
    open_to_close_bracket = {
        "(": ")",
        "{": "}",
        "[": "]",
    }
    buffer = []
    for c in s:
        if c in open_to_close_bracket:
            buffer.append(c)
            continue

        if not buffer or open_to_close_bracket[buffer.pop()] != c:
            return False

    return len(buffer) == 0


if __name__ == "__main__":
    # assert isValid("()")
    assert isValid("({[]{}})")
    assert isValid("()[]{}")
    assert not isValid("(]")
