import numpy as np

data = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])

print(data.sum())

# Sum along axis 0 (column totals)
column_totals = data.sum(axis=0)
print("Breaches per client:", column_totals)

row_total = data.sum(axis=1)
print("Par year : ", row_total.reshape(4,1))



# Min and max of entire array
print("Minimum value:", data.min())
print("Maximum value:", data.max())



# Mean of entire array
print("Average breaches per year/client:", data.mean())

# Mean per column (axis=0)
print("Average breaches per client:", data.mean(axis=0))

# Mean per row (axis=1)
print("Average breaches per year:", data.mean(axis=1))


# Without keepdims
row_sums = data.sum(axis=1)
print("Row sums shape (no keepdims):", row_sums.shape)

# With keepdims=True
row_sums_kept = data.sum(axis=1, keepdims=True)
print("Row sums shape (keepdims=True):", row_sums_kept.shape)
print("Row sums with keepdims:\n", row_sums_kept)


#Cumulative Sums
# Cumulative sum along axis 0 (running total per client over years)
cumsum_by_year = np.cumsum(data, axis=0)
print("Cumulative breaches per client by year:\n", cumsum_by_year)