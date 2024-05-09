import math

def g(x, y):
    return x - math.cos(y)

def h(x):
    return -math.sin(x)

x_a = 0
x_b = 2


for i in range(5):
    h_x_a = h(x_a)
    h_x_b = h(x_b)
    
    x_c = (x_a + x_b) / 2
    h_x_c = h(x_c)
    
    diff = abs(x_b - x_a)
    
    g_x_a = g(x_a, h_x_a)
    g_x_c = g(x_c, h_x_c)
    
    if g_x_a * g_x_c > 0:
        x_a = x_c
    else:
        x_b = x_c
    
    print(f"{i+1}: x_a={x_a}, x_b={x_b},x_c={x_c}, |x_b - x_a|={diff}, g(x_a, y_a)={g_x_a}, g(x_c, y_c)={g_x_c}, h(x_a)={h_x_a}, h(x_b)={h_x_b}, h(x_c)={h_x_c}")

