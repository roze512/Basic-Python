def sum_natural_numbers(n):
    total = 0
    counter = 1

    while counter <= n:
        total += counter
        counter += 1

    return total

print(sum_natural_numbers(10))
