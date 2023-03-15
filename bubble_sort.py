import matplotlib.pyplot as plt
import numpy as np
import random

amount = 15
# TODO accept user input here?
lst = np.random.randint(
    0, 100, amount
)  # create random list of 15 elements between 0 and 100
x = np.arange(0, amount, 1)

n = len(lst)

# bubble sort
for i in range(n):
    for j in range(0, n - i - 1):
        plt.bar(x, lst)
        plt.pause(0.01)  # not too small
        plt.clf()  # clear figure
        if lst[j] > lst[j + 1]:  # TODO change color of current bar i.e., lst[j]
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
plt.show()
