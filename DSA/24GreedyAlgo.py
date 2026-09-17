# fractional Knaspack Greedy algoritms

def Fractional_knapsack(Items_wt, price, capacity):
    n = len(Items_wt)

    #items = [(24,3,7),(12,4,3),(10,5,2)]
    items = [ (price[i],Items_wt[i], price[i]/Items_wt[i]) for i in range(n)]

    for i in range(n):
        for j in range(i+1, n):
            if(items[1][2] < items[j][2]):
                items[i], items[j] = items[j], items[1]

    profit = 0.0

    for price, items_wt, perKgPrice in items:
        if (capacity >= items):
            capacity = capacity-items_wt
            profit = profit + price

        else:
            profit =  profit + perKgPrice * capacity

    print ("total profit =", profit) 



price = [24, 21, 12, 10]
items_wt= [7, 3, 4, 5]  

Fractional_knapsack(items_wt, price, capacity = 20)