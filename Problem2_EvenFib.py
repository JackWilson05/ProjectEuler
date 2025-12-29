def sum_fib_even_less_than_n(n):
    # 1, 2, 3, ...

    cur = 1
    prev = 0
    total = 0

    while cur < n:
        if cur % 2 == 0:
            total += cur
        
        temp = cur

        cur = prev + cur
        prev = temp

    return total

# given even and prev, we need to form next even
# F_2k, F_2k-2 -> F_2k+2
# F_2k+1 + F_2k
# F_2k + F_2k + F_2k-1
# F_2k + F_2k-1 + F_2k-1 F_2k-2
def faster_version(n):
    cur = 2
    prev = 0

    total = 0

    while cur < n:
        total += cur

        temp  = cur
        cur = 4 * cur + prev
        prev = temp

    return total


if __name__ == "__main__":
    print(sum_fib_even_less_than_n(4000000))
    print(faster_version(4000000))