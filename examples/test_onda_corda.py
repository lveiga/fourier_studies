from pylab import *
from numpy import pi, arange
x = arange (0, 2, 0.01)
y = 0.5 - 1/pi * 1 * sin(pi*x)
for n in range (3,2,1):
    y = y + 1/2 - 1/pi * 1/n * sin(n*pi*x)

plot (x,y, 'g-',label= 'n=1')
leg = legend (fancybox=True, loc='upper left')
leg.get_frame().set_alpha(0.15)
ylabel ('f(x)')
grid (False)

x = arange (0, 2, 0.01)
y = 0.5 - 1/pi * 1 * sin(pi*x)
for n in range (3,10,1):
    y = y + 1/2 - 1/pi * 1/n * sin(n*pi*x)

plot (x,y, 'b-',label= 'n=9')
leg = legend (fancybox=True, loc='upper left')
leg.get_frame().set_alpha(0.15)

x = arange (0, 2, 0.01)
y = 0.5 - 1/pi * 1 * sin(pi*x)
for n in range (3,18,1):
    y = y + 1/2 - 1/pi * 1/n * sin(n*pi*x)

plot (x,y, 'k-',label= 'n=17')
leg = legend (fancybox=True, loc='upper left')
leg.get_frame().set_alpha(0.15)

x = arange (0, 2, 0.01)
y = 0.5 - 1/pi * 1 * sin(pi*x)
for n in range (3,26,1):
    y = y + 1/2 - 1/pi * 1/n * sin(n*pi*x)

plot (x,y, 'c-',label= 'n=25')
leg = legend (fancybox=True, loc='upper left')
leg.get_frame().set_alpha(0.15)

ylabel ('f(x)')

x = arange (0, 2, 0.01)
y = 0.5 - 1/pi * 1 * sin(pi*x)
for n in range (3,76,1):
    y = y + 1/2 - 1/pi * 1/n * sin(n*pi*x)

plot (x,y, 'g-',label= 'n=75')
leg = legend (fancybox=True, loc='upper left')
leg.get_frame().set_alpha(0.5)

xlabel ('x')

x = arange (0, 2, 0.01)
y = 0.5 - 1/pi * 1 * sin(pi*x)
for n in range (3,96,1):
    y = y + 1/2 - 1/pi * 1/n * sin(n*pi*x)

plot (x,y, 'm-',label= 'n=95')
leg = legend (fancybox=True, loc='upper left')
leg.get_frame().set_alpha(0.15)

show ()