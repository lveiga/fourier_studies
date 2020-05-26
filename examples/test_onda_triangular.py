from pylab import *
from numpy import pi, arange
x = arange (-3, 3, 0.01)
y = 4./pi**2 * 1 * sin(pi*x)
for n in range (3,29,2):
    y = y + 4./pi**2 * ((-1)**n-1/2)/n**2 * sin(n*pi*x)

plot(x,y, 'b-', label='n=29')
title ('Onda Triangular')
legend(fancybox=True, loc='upper left')
xlabel ('t')
ylabel ('x')
grid (False)

show ()