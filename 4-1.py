import numpy as np

# 関数の定義
def f(x, y):
    return np.sin(x) + y

def g(x, y):
    return x - np.cos(y)

# ヤコビ行列の定義
def jacobian(x, y):
    return np.array([[np.cos(x), 1],
                     [1, np.sin(y)]])

# ニュートン法の実装
def newton_method(x_init, y_init, tol=1e-6, max_iter=100):
    x = x_init
    y = y_init
    for i in range(max_iter):
        f_val = np.array([f(x, y), g(x, y)])
        jacobian_inv = np.linalg.inv(jacobian(x, y))
        delta = -jacobian_inv.dot(f_val)
        x += delta[0]
        y += delta[1]
        if np.linalg.norm(delta) < tol:
            break
    return x, y

# 初期値を設定
x1, y1 = 0, 0

# 初期値(x1, y1)での解
x2, y2 = newton_method(x1, y1)

# 初期値(x2, y2)での解
x3, y3 = newton_method(x2, y2)

print(f"x1={x1}, y1={y1}")
print(f"x2={x2}, y2={y2}")
print(f"x3={x3}, y3={y3}")

