from typing import List


def doOperation(operation: str, op1: int, op2: int) -> int:
    match operation:
        case "+":
            return op1 + op2
        case "-":
            return op1 - op2
        case "*":
            return op1 * op2
        case "/":
            return int(op1 / op2)
        case _:
            raise ValueError(f"invalid operation value {operation}")


def evalRPN(tokens: List[str]) -> int:
    buffer = []
    operands = {"+", "-", "*", "/"}
    for token in tokens:
        if token in operands:
            op2, op1 = buffer.pop(), buffer.pop()
            buffer.append(doOperation(token, op1, op2))
        else:
            buffer.append(int(token))

    return buffer.pop()


if __name__ == "__main__":
    # assert evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert (
        evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
        == 22
    )
