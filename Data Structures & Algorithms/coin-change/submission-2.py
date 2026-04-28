class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for curr_amount in range(1, amount + 1):
            for coin in coins:
                if curr_amount - coin >= 0:
                    dp[curr_amount] = min(dp[curr_amount], 1 + dp[curr_amount - coin])
        return dp[amount] if dp[amount] != amount + 1 else -1