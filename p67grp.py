from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
color = ['y', 'r', 'b', 'c', 'm', 'g', 'k']
color1 = np.array(color)
df = pd.read_csv("covid.csv")
x = list(df.iloc[:5, 0])
y = list(df.iloc[:5, 1])
a = list(df.iloc[:5, 2])
b = list(df.iloc[:5, 3])
c = list(df.iloc[:5, 4])
d = list(df.iloc[:5, 5])
e = list(df.iloc[:5, 6])
print(x)
print(y)
print(c)

#fig, ax = plt.subplots()
plt.plot(x, y, color=color[0], marker="x")
plt.plot(x, a, color=color[1], marker="x")
plt.plot(x, b, color=color[2], marker="x")
plt.plot(x, c, color=color[3], marker="x")
plt.plot(x, d, color=color[4], marker="x")
plt.plot(x, e, color=color[5], marker="x")

plt.xlabel("MONTHS")
plt.ylabel("COVID CASES")
plt.title("---- COVID TRACKING* ----")

plt.show()
