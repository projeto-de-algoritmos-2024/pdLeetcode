class Solution(object):
    def sellingWood(self, m, n, prices):
        """
        :type m: int
        :type n: int
        :type prices: List[List[int]]
        :rtype: int
        """
        price_map = {(h, w): p for h, w, p in prices}
    
        memo = [[-1] * (n + 1) for _ in range(m + 1)]
    
        def dp(h, w):
            if memo[h][w] != -1:
                return memo[h][w]
            
            max_profit = price_map.get((h, w), 0)
            
            for cut in range(1, h):
                max_profit = max(max_profit, dp(cut, w) + dp(h - cut, w))
            
            for cut in range(1, w):
                max_profit = max(max_profit, dp(h, cut) + dp(h, w - cut))
            
            memo[h][w] = max_profit
            return max_profit
        
        return dp(m, n)
        