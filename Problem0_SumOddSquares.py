def calculate_sum_odd_squares_of_n(n):
    total = 0
    for i in range(1, n, 2):
        total += i ** 2

    return total

# MORE EFFICIENT WAY???
# 1 9 25 49

# 4k^2 - 4k + 1
# (n + 1) * n / 2

def calculate_faster(n):
    return n * (2 * n + 1) * (2 * n - 1) / 3

if __name__ == "__main__":
    print(calculate_sum_odd_squares_of_n(550000))
    print(calculate_faster(550000))
    print(calculate_sum_odd_squares_of_n(550000) - calculate_faster(550000))