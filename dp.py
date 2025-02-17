import time

def fibd(n, memo):
    if n in memo:
        return memo[n]
    memo[n] = fibd(n - 1, memo) + fibd(n - 2, memo)
    return memo[n]

def fibdp(n, memo):
    if n in memo:
        return memo[n]
    if (n - 1) in memo:
        n1 = memo[n - 1]
    else:
        n1 = fibdp(n - 1, memo)
    if (n - 2) in memo:
        n2 = memo[n - 2]
    else:
        n2 = fibdp(n - 2, memo)
    memo[n] = n1 + n2
    return memo[n]

def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

def fibt(n, tab = {0: 0, 1: 1, 2: 1}):
    i = 3
    while i <= n:
        tab[i] = tab[i-2] + tab[i-1]
        i+=1
    return tab[n]

k = 10000

# Measure fibt
start = time.perf_counter()
result_fibt = fibt(k)
end = time.perf_counter()
print(f"fibt(100) = {result_fibt}")
print(f"Time for fibt: {end - start:.6f} seconds\n")

# Measure fibd
memo_fibd = {0: 0, 1: 1, 2: 1}
start = time.perf_counter()
result_fibd = fibd(k, memo_fibd)
end = time.perf_counter()
print(f"fibd(100) = {result_fibd}")
print(f"Time for fibd: {end - start:.6f} seconds\n")

# Measure fibdp
memo_fibdp = {0: 0, 1: 1, 2: 1}
start = time.perf_counter()
result_fibdp = fibdp(k, memo_fibdp)
end = time.perf_counter()
print(f"fibdp(100) = {result_fibdp}")
print(f"Time for fibdp: {end - start:.6f} seconds\n")



# The naive recursive approach (fib) is too slow for n=100
# Uncommenting the following will result in an extremely long execution time!
# start = time.perf_counter()
# result_fib = fib(100)
# end = time.perf_counter()
# print(f"fib(100) = {result_fib}")
# print(f"Time for fib: {end - start:.6f} seconds")