"""
import matplotlib.pylab as plt
import numpy as np
from sklearn import linear_model as lm, datasets as db, model_selection as ms

dia = db.load_diabetes()


x_train, x_test, y_train, y_test = \
    ms.train_test_split(dia.data, dia.target, test_size = 0.2)

reg = lm.LinearRegression()
reg.fit(x_train, y_train)

y_pred = reg.predict(x_test)

plt.plot(y_test, y_pred, ".")

x = np.linspace(0, 300, 101)
y = x
plt.plot(x, y)
plt.show()
"""
import matplotlib.pylab as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import datasets
# 당뇨병 데이터 세트를 적재한다.
diabetes = datasets.load_diabetes()
# 학습 데이터와 테스트 데이터를 분리한다.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(diabetes.data, diabetes.target,
test_size=0.2, random_state=0)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
# 실제 데이터와 예측 데이터를 비교해보자.
plt.plot(y_test, '.', color = "red")
plt.plot(y_pred, '.', color = "blue")

plt.show()