from typing import List


def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    l = 0
    for r in range(1, len(prices)):
        max_profit = max(max_profit, prices[r] - prices[l])
        if prices[l] > prices[r]:
            l = r

    return max_profit


if __name__ == "__main__":
    assert maxProfit([7, 1, 5, 3, 6, 4]) == 5
