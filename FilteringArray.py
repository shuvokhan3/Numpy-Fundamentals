import numpy as np

# #Boolean musking
# array_value = np.array([1,2,3,4])
# mask = array_value % 2 == 0
# print(mask)
#
# #filtering with funcy indexing
# value2 = np.array([1,2,3,4,5,6,7,8,9])
# mask2 = value2 % 2 == 0
#
# #use the musk finter the array
# even_num = value2[mask2]
# print(even_num)
#
# #can also be done in one line
# even_num2 = value2[value2 % 2 == 0]
# print(even_num2)

product_data = np.array([
    [12,23],
    [13,45],
    [14,56],
    [15,67],
    [16,78]
])

#boolean musking for where product quantity is even number
mask_qt = product_data[:,1] % 2 == 0
print(mask_qt)

#get all the product id
product_id = product_data[: , 0]

#find all the even product id row and col
even_product_id = mask_qt == 1

#print all product id where the proudct quentity data is true
print(product_id[even_product_id])



# Product IDs in first column, quantities in second column
inventory = np.array([
    [101, 24],
    [102, 31],
    [103, 27],
    [104, 22]
])

print("Inventory data:\n", inventory)

# Create mask for even quantities (second column)
even_qty_mask = inventory[:, 1] % 2 == 0
print("Even quantity mask:", even_qty_mask)

# Get product IDs (first column) where quantity is even
products_even_qty = inventory[even_qty_mask, 0]
print("Product IDs with even quantities:", products_even_qty)


#find all the value of this array where value are grater than 20
numbers = np.array([10, 25, 30, 45, 50])

indeses = np.where(numbers >= 20)

print(numbers[indeses])



grid = np.array([
    [5, 3, 0, 0, 7],
    [6, 0, 0, 1, 9],
    [0, 9, 8, 0, 0]
])

row_indices, col_indices = np.where(grid == 0)
print(row_indices, col_indices)


for row, col in zip(row_indices, col_indices):
    print(row, col)


























