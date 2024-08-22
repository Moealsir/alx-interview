#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize dp array with infinity for all totals greater than 0
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins needed to make total of 0
    dp[0] = 0

    # Build up dp array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If we haven't found a solution, dp[total] will still be infinity
    return dp[total] if dp[total] != float('inf') else -1


# Test cases
if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))  # Expected output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Expected output: -1
