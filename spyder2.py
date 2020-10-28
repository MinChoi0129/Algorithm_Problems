import matplotlib.pylab as plt
import numpy as np
from sklearn import linear_model as lm

x_train = [[2011],[2012],[2013],[2014],[2015],[2016]]
y_train = [396.8,399.9,402.4,404.6,407,409.9]

x_test = [[2017],[2018],[2019]]
y_test = [412.2, 415.2, 417.9]

reg = lm.LinearRegression()
reg.fit(x_train, y_train)

y_pred = reg.predict(x_test)

plt.plot(y_test, y_pred, '.', color = "red")

x = np.linspace(410, 420, 101)
y = x

plt.plot(x, y, color = "blue")

print(reg.predict([[2010]]))
print(reg.predict([[2020]]))

print(reg.coef_)
print(reg.intercept_)
print(reg.score(x_train, y_train))

plt.show()