#1.412389
import math

def f(x):
    return x**2 - 1 - math.sin(x)

def df(x):
    return 2*x - math.cos(x)

def ddf(x):
    return 2 + math.sin(x)

X1 = 3.0

X2 = X1 - (2*f(X1)*df(X1))/(2*(df(X1)**2)-f(X1)*ddf(X1))
X3 = X2 - (2*f(X2)*df(X2))/(2*(df(X2)**2)-f(X2)*ddf(X2))


print(f"X1={X1},f(X1)={f(X1)},df(X1)={df(X1)},ddf(X1)={ddf(X1)},X2={X2},f(X2)={f(X2)},df(X2)={df(X2)},ddf(X2)={ddf(X2)},X3={X3},f(X3)={f(X3)},df(X3)={df(X3)},ddf(X3)={ddf(X3)}")

