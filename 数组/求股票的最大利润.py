def maxprofit(prices):
    if not prices or len(prices)<2:
        return 0
    min_p = prices[0]
    max_p = prices[1] - min_p
    for i in range(2,len(prices)):
        if prices[i-1] < min_p:
            min_p = prices[i-1]
        if prices[i] - min_p >max_p:
            max_p = prices[i] - min_p
    if max_p < 0:
        return 0
    return max_p


