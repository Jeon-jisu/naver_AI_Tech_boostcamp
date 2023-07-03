import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000000)
n = int(input())


def matrix_max(A, B):
    temp = [[0] * 2 for i in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                temp[i][j] += (A[i][k] * B[k][j]) % 1000000007
    return temp


def matrix_pow(n, M):
    if n == 1:
        return M
    elif n % 2 == 0:
        tmp = matrix_pow(n // 2, M)
        return matrix_max(tmp, tmp)
    else:
        tmp = matrix_pow(n - 1, M)
        ans = matrix_max(tmp, M)
        return ans


K = [[1, 1], [1, 0]]
if n == 1:
    print("1")
else:
    print(matrix_pow(n - 1, K)[0][0] % 1000000007)
