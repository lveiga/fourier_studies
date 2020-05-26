from pylab import *
from numpy import pi, arange
x = arange (-pi, pi, 0.01)
a = 5*(e**(-(0.9/(2*0.3))*x)*cos(sqrt((2.5/0.3)-((0.9**2)/(4*(0.3**2))))*x))
b = 5*(e**(-(0.6/(2*0.3))*x)*cos(sqrt((2.5/0.3)-((0.6**2)/(4*(0.3**2))))*x))
c = 5*(e**(-(0.3/(2*0.3))*x)*cos(sqrt((2.5/0.3)-((0.3**2)/(4*(0.3**2))))*x))

plot (x, a, 'b-', label = 'b= 0,900 kg/s')
plot (x, b, 'g-', label = 'b= 0,600 kg/s')
plot (x, c, 'r-', label = 'b= 0,300 kg/s')
title (u'Comparação de oscilações com amortecimentos')
legend (fancybox=True, loc='upper right')
xlabel ('t')
ylabel ('x')
grid (True)

show ()
