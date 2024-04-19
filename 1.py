import math
def f(x):
    return (x**2)-2
    
a = 0
b = 2

for i in range(5):
    c = (a + b) / 2
    diff = abs(b - a)
    f_a = f(a)
    f_c = f(c)
    f_ac=f_a * f_c 
    
    if f_a * f_c > 0:
        a = c
    else:
        b = c
    
    print(f"{i+1}: a={a}, b={b},c={c}, |b-a|={diff}, f(a)={f_a}, f(c)={f_c},f(a)f(c)={f_ac}")

