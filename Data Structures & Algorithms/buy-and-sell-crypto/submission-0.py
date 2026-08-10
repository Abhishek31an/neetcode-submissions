class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=1
        cp=prices[0]
        maxm=0
        profit=0
        while i<len(prices):
            profit=prices[i]-cp
            if profit>maxm:
                maxm=profit
            if prices[i]<cp:
                cp=prices[i]
            i+=1
        return maxm
            