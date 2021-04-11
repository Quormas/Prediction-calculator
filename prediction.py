import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.metrics import r2_score

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

plt.scatter(x, y, color="blue")

arr = []

for i in range(6):
    poly_i = make_pipeline(PolynomialFeatures(degree=i), Ridge())
    poly_i.fit(x,y)
    arr.append(r2_score(y, poly_i.predict(x)))
    
deg = arr.index(max(arr))
    
poly = make_pipeline(PolynomialFeatures(degree=deg), Ridge())
poly.fit(x,y)
y_poly = poly.predict(x)
    
plt.plot(x, y_poly, color="red")

pred_x = np.array( [len(x)] ).reshape((-1, 1))
pred_y = poly.predict(pred_x)

plt.scatter(pred_x, pred_y, color="red")

plt.title(pred_y[0], fontsize=15)

plt.show()
