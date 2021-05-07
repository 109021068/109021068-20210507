import numpy as np
import random as rand

np.zeros((2, 3))
x = np.ones((2, 3, 4)) * 128
#print(x)
np.arange(1, 10, 2)
x = np.linspace((1, 10, 2))

fileName = "out2.npy"
with open(fileName, "wb") as fp:
    np.save(fp, x1)
print("--------- 我是分隔線 ------")