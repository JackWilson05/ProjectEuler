import math

def find_max_prime_fac(n):
    # for each factor up to sqrt n see if divides
    # but only check primes (skip if alr in checked)
    
    # start by dividing by 2 until cant anymore

    # then divide by odds up to sqrt n

    # if anything left then thats highest, else its last

    largest = None

    while n % 2 == 0:
        largest = 2
        n = n//2

    div = 3
    while div ** 2 < n:
        while n % div == 0:
            largest = div
            n = n//div

        div += 2

    if n > 1:
        largest = n

    return largest



if __name__ == "__main__":
    print(find_max_prime_fac(600851475143))