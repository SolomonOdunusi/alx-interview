#!/usr/bin/python3
"""This module makes change"""


def makeChange(coins, total):
    """Given a pile of coins of
    different values, determine
    the fewest number of coins
    needed to meet a given amount
    total
    """
    # If total is 0 or less, return 0
    if total <= 0:
        return 0
    
    # Create a list to store the minimum number of coins needed to make each total from 0 to total
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0
    
    # Iterate through each coin value
    for coin in coins:
        # Update the min_coins list for each total from coin value to total
        for i in range(coin, total + 1):
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)
    
    # If the min_coins list at the total is still infinity, it means the total cannot be met by any number of coins you have
    if min_coins[total] == float('inf'):
        return -1
    else:
        return min_coins[total]
