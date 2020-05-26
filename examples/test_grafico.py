import matplotlib.pyplot as plt

x = []
y = []

dataset = open('files/dolar.txt', 'r')

for line in dataset:
    line = line.strip()
    bla, bla1 = line.split(',', 1)
    x.append(bla)
    y.append(bla1)


dataset.close()

plt.plot(x, y)

plt.title('example')
plt.xlabel('x label')
plt.ylabel('y label')

plt.show()