from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np
import random

losowe = []

ile_rzutow = int(input("Podaj liczbę rzutów kostką: "))

for x in range(ile_rzutow):
    losowe.append (random.randint(1,6))

l1 = losowe.count(1)
l2 = losowe.count(2)
l3 = losowe.count(3)
l4 = losowe.count(4)
l5 = losowe.count(5)
l6 = losowe.count(6)

x = np.arange(6)
money = [l1, l2, l3, l4, l5, l6]
fig, ax = plt.subplots()
ax.set_xlabel('Liczba oczek')
ax.set_ylabel('Liczba wystąpień danej liczby')
ax.set_title('Wyniki rzutów kostką')
plt.bar(x, money)
plt.xticks(x, ('1', '2', '3','4','5','6'))
plt.show()