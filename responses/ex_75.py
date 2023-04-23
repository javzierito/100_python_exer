import numpy as np
import matplotlib.pyplot as plt
text1 = np.loadtxt("responses/text11.txt", skiprows=1)
with open("responses/text11.txt", "r") as file_handler:
    data = file_handler.read()

data = data.split('\n')

x = [row.split()[0] for row in data]
y = [row.split()[1] for row in data]

fig = plt.figure()

plt.plot(x,y)

plt.show()