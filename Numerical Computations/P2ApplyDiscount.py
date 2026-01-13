import numpy as np

#4 shop 3 product

product_shop = [
  [100, 110, 120, 105],
  [150, 160, 140, 155],
  [200, 210, 190, 205]
]

discounts_value = [10, 15, 20, 5]

def apply_discounts(prices: list[list[int]], discounts: list[int]) -> float:
    prices = np.array(prices)
    discounts = np.array(discounts)

    # Convert discount percentages to multipliers - vectorized operation
    multipliers = 1 - discounts / 100


    # Broadcasting: prices (3, 4) * multipliers (4,) → result (3, 4)
    # Each column is multiplied by corresponding multiplier
    discounted = prices * multipliers


    result = round(float(discounted.max()), 2)
    return result

res = apply_discounts(product_shop, discounts_value)
print(res)
