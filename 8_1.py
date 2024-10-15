import matplotlib.pyplot as plt 
import numpy as np
file = open("Вольт-временная_хар7_1.txt", "r")
A1=np.array([x for x in (file).readlines()])
A=[float(x[:-1])*3.3/256 for x in A1[2:]]
t=float(A1[0][4:-1])
V=float(A1[1][4:-1])
print(A)
T=[t*x for x in range(len(A))]
plt.grid(True, linewidth=0.5)
plt.plot([t*x for x in range(len(A))], A)
plt.xlabel('Время  t, c', fontsize=14, family='serif')
plt.ylabel('Напряжение на кон-ре U, B', fontsize=14, family='serif')
plt.xticks(np.arange(min(T), max(T)+1, 0.5))
plt.yticks(np.arange(min(A), max(A), 0.2))
plt.show()