class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        primes = [True] * (n + 1)
        prime_cnt = 0
        for i in range(2, n + 1):
            if primes[i]:
                prime_cnt += 1
                for j in range(i + i, n + 1, i):
                    primes[j] = False

        mod = (10 ** 9 + 7)
        ans = (math.factorial(prime_cnt) % mod * math.factorial(n-prime_cnt) % mod) % mod
        return int(ans)