"""
Dynamic Programming Example: Coin Change Problem

This script demonstrates an efficient method to count the number of unique ways to form 100 cents
using the coin denominations [1, 10, 15, 50].

Approach:
- Use a bottom-up dynamic programming (tabulation) technique.
- dp[i] will store the number of ways to make amount i.
- Initialize dp[0] = 1 since there is exactly one way to make 0 cents (use no coins).
- For each coin, update dp for all amounts from coin value up to 100.

Run this script directly to see the result.
"""

def count_ways_to_make_amount(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1  # Base case

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin]

    return dp[amount]


def main():
    coins = [1, 10, 15, 50]
    amount = 100
    ways = count_ways_to_make_amount(coins, amount)
    print(f"Number of ways to make {amount} cents with coins {coins}: {ways}")

    # Basic correctness check (known result or sanity check)
    # Since 1-cent coin is included, ways should be > 0
    assert ways > 0, "The number of ways should be positive."


if __name__ == '__main__':
    main()
