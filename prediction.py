import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline


file = open("data.txt", "r")
data = file.read().split("\n")

data = list(filter(lambda x: x != '', data))

data_x = []
data_y = []

for i in range(len(data)):
    data_x.append(i) 
    data_y.append(float(data[i]))

x = np.array(data_x).reshape((-1, 1))
y = np.array(data_y)

print(x)
print(y)

plt.scatter(x, y, color="blue")

poly = make_pipeline(PolynomialFeatures(degree=4), Ridge())
poly.fit(x,y)

y_poly = poly.predict(x)

plt.plot(x, y_poly, color="red")

pred_x = np.array( [len(x)] ).reshape((-1, 1))
pred_y = poly.predict(pred_x)

plt.scatter(pred_x, pred_y, color="red")

plt.title(pred_y, fontsize=15)

plt.show()
