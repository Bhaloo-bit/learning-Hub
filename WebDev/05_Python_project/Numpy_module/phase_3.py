## Advance operation with Busniess Examples

# Data structures : [restaurant_id, 2021, 2022, 2023, 2024]
import numpy as np
#%%
import matplotlib.pyplot as plt

sales_data = np.array([
    [1, 150000, 180000, 220000, 250000], #Paradise Biryani
    [2, 120000, 140000, 160000, 190000], #Beijing Bites  
    [3, 200000, 230000, 260000, 300000], #Pizza Hub
    [4, 180000, 210000, 240000, 270000], #BUrger Point
    [5, 160000, 185000, 205000, 230000]  #Chai wala
])

print("===== Zomato sales analysis =====")
#print("\n sales data shape", sales_data.shape)
#print("\n sample data for 1st 3 restaurent: ", sales_data[:3])


# total sales per year

#print(np.sum(sales_data, axis=0))
yearly_total = (np.sum(sales_data[:, 1:], axis = 0))
#print(np.sum(yearly_total))

'''
===== Zomato sales analysis =====
[     15  810000  945000 1085000 1240000]
4080000
'''
# minimun sales per restau

mini_sales = np.min(sales_data[:,1:], axis= 1)
#print(mini_sales)


# maximun sales per year 
max_sales = np.max(sales_data[:, 1:], axis = 0)
#print(max_sales)

# avg sales per restaurent 

avg_sales = np.average(sales_data[:, 1:], axis =1)
#print(avg_sales)

# cumutive sum

cumsum = np.cumsum(sales_data[:, 1:], axis =1)
#print(cumsum)

plt.figure(figsize=(10,6))
plt.plot(np.average(cumsum, axis = 0))
plt.title("Average cumulative sales accross all restaurent")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# Vector 

vector1 = np.array([1, 2, 3, 4, 5])
vector2 = np.array([6, 7, 8, 9, 10])

print("Vector sum :", vector1 + vector2)  # matrix addition
print("Vector multiplication :", vector1 * vector2) # matrix multiplication



# vaporization

restaurant_types = np.array(['biryani','chinese','pizza','burger','cafe'])
vactorized_upper = np.vectorize(str.upper)
print("vactorized Upper", vactorized_upper(restaurant_types))

# broadcast 

monthy_avg = sales_data[:, 1:] / 12 # broadcaasting it's dividing  each elements of the matrix array
print(monthy_avg)