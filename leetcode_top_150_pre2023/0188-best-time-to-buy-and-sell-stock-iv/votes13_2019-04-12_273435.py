cash[i+1][k] = max(cash[i][k], asset[i][k-1] - prices[i])
asset[i+1][k] = max(asset[i][k], cash[i+1][k] + prices[i])