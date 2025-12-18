def coin_change(coins, amount):
    """
    Coin Change Problem using Dynamic Programming.
    Finds the fewest number of coins that you need to make up that amount.
    Returns -1 if that amount of money cannot be made up by any combination of the coins.
    """
    # dp[i] will be storing the minimum number of coins for amount i
    # Initialize dp array with amount + 1 (infinity equivalent in this context)
    dp = [amount + 1] * (amount + 1)
    
    # Base case: 0 coins are needed to make amount 0
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[amount] is still amount + 1, it means we couldn't find a solution
    return dp[amount] if dp[amount] != amount + 1 else -1

if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    print(f"Coins: {coins}, Amount: {amount}")
    result = coin_change(coins, amount)
    print(f"Minimum coins required: {result}") # Expected 3 (5 + 5 + 1)

    coins2 = [2]
    amount2 = 3
    print(f"\nCoins: {coins2}, Amount: {amount2}")
    result2 = coin_change(coins2, amount2)
    print(f"Minimum coins required: {result2}") # Expected -1
