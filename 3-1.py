# 1.416667

def f(x):
    return x**2 - 2

def df(x):
    return 2*x

X1 = 2

X2 = X1 - f(X1) / df(X1)
X3 = X2 - f(X2) / df(X2)

print(f"X1 = {X1},f(X1)={f(X1)} ,df(X1)={df(X1)} ,X2 = {X2} ,f(X2)={f(X2)},df(X2)={df(X2)}, X3 = {X3},f(X3)={f(X3)},df(X3)={df(X3)}")


