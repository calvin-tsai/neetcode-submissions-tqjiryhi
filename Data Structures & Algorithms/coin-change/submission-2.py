class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # 0 ... amount
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        # T: O(m*n)
        # S: O(m) 
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        return dp[amount] if dp[amount] <= amount else -1

