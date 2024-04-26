def f(x):
    return x**2 - 2

X1 = 2.5
X2 = 2

X3 = X2 - ((X2 - X1) / (f(X2) - f(X1)) * f(X2))
X4 = X3 - ((X3 - X2) / (f(X3) - f(X2)) * f(X3))  

print (f"X1={X1},f(X1)={f(X1)},X2={X2},f(X2)={f(X2)},a2={(X2 - X1) / (f(X2) - f(X1))},X3={X3},f(X3)={f(X3)},a3={(X3 - X2) / (f(X3) - f(X2))},X4={X4},f(X4)={f(X4)},a4={(X4 - X3) / (f(X4) - f(X3))}")

