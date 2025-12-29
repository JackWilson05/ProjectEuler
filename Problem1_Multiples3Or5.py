# do all multiples of 3 + multiples of 5  - multiples of 15
# inclusion exclusion
def calculate_multiples_of_k_up_to_n(k, n):
    # sum 1 to n = (n + 1)(n / 2)
    # n = n // k
    # then do k * sum 1 to n

    new_n = n // k
    return k * (new_n + 1) * (new_n // 2)


if __name__ == "__main__":
    print(calculate_multiples_of_k_up_to_n(3, 999) + calculate_multiples_of_k_up_to_n(5, 999) - calculate_multiples_of_k_up_to_n(15, 999))