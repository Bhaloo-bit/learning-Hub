# knapsack recursion approach
'''
def knapsack_recursive(weight, values, capacity, n):
    if n == 0 or capacity ==0:
        return 0

    if weight[n-1]> capacity:
        return knapsack_recursive(weight, values, capacity, n-1)

    include = values[n-1] +knapsack_recursive(
        weight, values, capacity- weight[n-1], n-1
    )
    exclude = knapsack_recursive(weight, values , capacity , n-1)

    return max(include, exclude)'''

 # knapsack optimize SP

def knapsack(wt, value, capacity):
    n = len(wt)

    dp =[[0]*(capacity+1) for _ in range(n+1)]

    for i in range(n+1):
        for w in range(1,capacity+1):
            if(wt[i-1] <=w):
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-wt[i-1]] + value[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    print("max profit it ", dp[n][capacity])

weights =[2,3,4,5]
values = [3,4,5,6]

knapsack(weights, values, capacity=5)

                    
    
        