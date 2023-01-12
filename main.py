# prices of newspaper
prices = {
    'TOI': [3, 3, 3, 3, 3, 5, 6],
    'Hindu': [2.5, 2.5, 2.5, 2.5, 2.5, 4, 4],
    'ET': [4, 4, 4, 4, 4, 4, 10],
    'BM': [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5],
    'HT': [2, 2, 2, 2, 2, 4, 4],
}

# calculate total cost for the week
for key in prices:
    prices[key] = sum(prices[key])

papers = list(prices.keys())

amount = int(input())

n = len(prices)

ans = []

# check all possible combinations
for i in range(n):
    for j in range(i+1, n):
        if prices[papers[i]] + prices[papers[j]] <= amount:
            ans.append({papers[i], papers[j]})
        
print(*ans)
    