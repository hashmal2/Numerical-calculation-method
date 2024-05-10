import numpy as np

# 拡大係数行列を定義
A = np.array([[1, -1, -2, 5],
              [1, -3, 2, 4],
              [4, 1, -2, 4]], dtype=float)

# 前進消去
n = len(A)
for i in range(n):
    # ピボット選択
    max_row = i
    for k in range(i+1, n):
        if abs(A[k, i]) > abs(A[max_row, i]):
            max_row = k
    A[[i, max_row]] = A[[max_row, i]]  # 行の入れ替え

    # 前進消去
    for j in range(i+1, n):
        ratio = A[j, i] / A[i, i]
        A[j] -= ratio * A[i]

# 後退代入
x = np.zeros(n)
for i in range(n-1, -1, -1):
    x[i] = (A[i, -1] - np.dot(A[i, i+1:n], x[i+1:])) / A[i, i]

print("Solution:")
for i in range(n):
    print(f"x_{i+1} =", x[i])

