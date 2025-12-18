import sys

def matrix_chain_order(p):
    """
    Matrix Chain Multiplication using Dynamic Programming.
    p: an array where matrix i has dimensions p[i-1] x p[i].
    n: number of matrices (len(p) - 1)
    """
    n = len(p) - 1
    
    # m[i, j] = Minimum number of scalar multiplications needed
    # to compute the matrix A[i]...A[j] = A[i..j] where
    # dimension of A[i] is p[i-1] x p[i]
    m = [[0 for x in range(n + 1)] for x in range(n + 1)]
    
    # cost is zero when multiplying one matrix.
    for i in range(1, n + 1):
        m[i][i] = 0
        
    # L is chain length.
    for L in range(2, n + 1):
        for i in range(1, n - L + 2):
            j = i + L - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                # q = cost/scalar multiplications
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    
    return m[1][n]

if __name__ == "__main__":
    # Matrix dimensions
    # A1: 1x2, A2: 2x3, A3: 3x4
    # p = [1, 2, 3, 4]
    arr = [1, 2, 3, 4, 3]
    size = len(arr)
    
    print(f"Matrix dimensions array: {arr}")
    print("Minimum number of multiplications is", matrix_chain_order(arr))
