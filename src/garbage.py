# -- coding: utf-8 --
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt


def actual_line(x):
    return 3.68 * x + (random.random() - 0.5) * 5


graphing_list = []
for i in range(20):
    x = random.randint(0, 20)
    y = actual_line(x)
    graphing_list.append((x, y))

df = pd.DataFrame(data=graphing_list, columns=["sq feet", "home price"])
df.plot(kind="scatter", x="sq feet", y="home price")
plt.show()
# initial slope guess
slope = 2
for i in range(12):
    # plt.figure(i)
    df.plot(kind="scatter", x="sq feet", y="home price")
    df["predicted"] = df["sq feet"] * slope
    residuals = df["home price"] - df["predicted"]
    sum_of_errors = residuals.sum()
    max_sq_feet = df["sq feet"].max()
    plt.plot([0, max_sq_feet], [0, max_sq_feet * slope], color="red")
    if sum_of_errors > 0:
        slope = slope + 0.2
    elif sum_of_errors < 0:
        slope = slope - 0.2
    print(i, slope)
    plt.scatter(df["sq feet"], df["predicted"], color="red")

plt.show()


def run_model(slope, x):
    return slope * x
