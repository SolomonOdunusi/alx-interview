#!/usr/bin/python3
"""Module for prime game"""


def isWinner(x, nums):
    # Find the maximum number to generate primes up to this number
    max_n = max(nums)
    
    # Sieve of Eratosthenes to find all primes up to max_n
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime
    p = 2
    while p * p <= max_n:
        if sieve[p]:
            for i in range(p * p, max_n + 1, p):
                sieve[i] = False
        p += 1
    primes = [i for i in range(max_n + 1) if sieve[i]]
    
    # Use this prime list to determine the winner of each game
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        # State tracking for each number from 1 to n
        playable = [False] * (n + 1)
        
        # Determine the playable numbers
        for prime in primes:
            if prime > n:
                break
            # If prime is within n, mark multiples as playable
            if sieve[prime]:
                for multiple in range(prime, n + 1, prime):
                    playable[multiple] = True
                    
        # Count playable numbers
        count_playable = sum(playable)
        
        # If the count of playable numbers is odd, Maria wins (since she starts)
        # If even, Ben wins (because the game ends on Maria's turn with no moves left)
        if count_playable % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    
    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
