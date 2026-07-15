prices = [50, 120, 0, 300, 80, 0, 150]

for price in prices:
    if price == 0:
        continue

    if price > 100:
        discounted_price = price - (price * 0.10)
        print(f"Discounted price: {discounted_price}")
    else:
        print(f"Price: {price}")
