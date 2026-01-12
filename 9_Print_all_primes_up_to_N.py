# Print all primes up to N

input_numer = int(input("enter a number - "))

def all_prime_numbers_up_to_N(num):
    count = 0
    if num < 2:
        print("number should be greater than 2")
        return
    for i in range(2,num+1):
        is_prime = True
        for j in range(2, int(i ** 0.5)+1):
            if i%j==0:
                is_prime = False
                break
        if is_prime==True:
            print(i)
            count+=1
    print("count - ",count)
                

all_prime_numbers_up_to_N(input_numer)


def all_primes_sieve(n):
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    print('is_prime: ', is_prime)
    is_prime[0] = is_prime[1] = False
    print('is_prime: ', is_prime)

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                print('j: ', j)
                is_prime[j] = False
            print('is_prime: ', is_prime)

    primes = [i for i in range(2, n + 1) if is_prime[i]]
    return primes


n = int(input("enter a number - "))
primes = all_primes_sieve(n)
print(primes)
print("count -", len(primes))
