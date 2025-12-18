def fibonacci_iterative(n):
    """
    Iterative approach to find nth Fibonacci number.
    Space Complexity: O(1)
    Time Complexity: O(n)
    """
    if n < 0:
        return "Incorrect input"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b

def fibonacci_recursive(n):
    """
    Naive recursive approach.
    Time Complexity: O(2^n) (Bad)
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_dp(n):
    """
    Dynamic Programming approach (Memoization).
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    f = [0] * (n + 1)
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

if __name__ == "__main__":
    n = 9
    print(f"Fibonacci({n}) iterative: {fibonacci_iterative(n)}")
    print(f"Fibonacci({n}) DP: {fibonacci_dp(n)}")
