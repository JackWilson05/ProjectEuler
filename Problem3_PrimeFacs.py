import math

def find_max_prime_fac(n):
    # for each factor up to sqrt n see if divides
    # but only check primes (skip if alr in checked)

    def sieve_of_erasthones(little_n):
        possible = [i for i in range(2, little_n + 2)]


        ind = 0
        while ind < len(possible):
            val = possible[ind]

            for j in range(ind + 1, len(possible)):
                if possible[j] % val == 0:
                    possible.pop(j)


            ind += 1

        return possible
    
    # iterate through sieve searching for maximum that is a factor
    # binary search for sqrt, then deccrease until you hit something 
    
    return sieve_of_erasthones(n)


if __name__ == "__main__":
    print(find_max_prime_fac(3))