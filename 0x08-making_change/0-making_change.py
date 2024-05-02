#!/usr/bin/python3
"""This module makes change"""


def makeChange(coins, total):
    """Determine the fewest number of coins
    needed to meet a given amount
    total
    """
    if(total <= 0):
        return 0

    placeholder = total + 1

    min_coin = {0: 0}

    for i in range(1, total + 1):
        min_coin[i] = placeholder

        for coin in coins:
            current = i - coin
            if current < 0:
                continue

            min_coin[i] = min(min_coin[current] + 1, min_coin[i])

    if min_coin[total] == total + 1:
        return -1

    return min_coin[total]
