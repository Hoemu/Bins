import matplotlib.pyplot as plt

x = range(2, 25, 2)

y = [15,13,14.5,17,20,25,26,24,22,18,15,11]

plt.figure(figsize = (5, 5))

k = [i for i in range(2, 24, 4)]
str = "time is {} h"

print(k)

plt.xticks(range(2, 24, 4), "", rotation = 90)

plt.plot(x, y)

plt.show()