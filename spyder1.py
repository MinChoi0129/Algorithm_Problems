import matplotlib.pylab as plt
from sklearn import linear_model as lm

x = [\
    [1985],[1986],[1987],[1988],[1989],[1990],[1991],[1992],[1993],[1994],[1995],[1996],\
    [1997],[1998],[1999],[2000],[2001],[2002],[2003],[2004],[2005],[2006],[2007],[2008],\
    [2009],[2010],[2011],[2012],[2013],[2014],[2015],[2016],[2017],[2018]\
]

y = [\
    31181,32239,33238,35448,37430,39240,39080,44291,47042,49416,50433,50962,52848,51291,\
    54238,58197,59287,63018,63721,64701,65529,65911,67870,68912,69779,72048,71579,73759,\
    75334,76611,76855,78194,78863,79153\
]

reg = lm.LinearRegression()
reg.fit(x, y)
y_pred = reg.predict(x)

plt.scatter(x, y)
plt.plot(x, y_pred, color = "red")

print(reg.predict([[2016]]))
print(reg.predict([[2017]]))
print(reg.predict([[2018]]))

print(reg.predict([[2020]]))

print(reg.coef_)
print(reg.intercept_)
print(reg.score(x, y))

plt.show()