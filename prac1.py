import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from statistics import  mean
style.use('ggplot')

data = pd.read_csv('Book_1.csv')
a = data[data.columns[0]].values
b = data[data.columns[-1]].values

xs = np.array(a, dtype=np.float64)
ys = np.array(b, dtype=np.float64)

def best_fit_line(xs,ys):
    m = ((mean(xs) * mean(ys))-mean(xs * ys)) / ((mean(xs) * mean(xs)) - mean(xs * xs))
    c = mean(ys) - m*mean(xs)
    return m,c

m,c = best_fit_line(xs,ys)
print("y = "+np.str_(m)+"x + "+np.str_(c))

regression_line = []
for x in xs:
    regression_line.append((m*x)+c)
    print(np.str(x) + "   " + np.str(m*x+c))
    
plt.scatter(xs,ys,color='#111111')
plt.plot(xs,regression_line)
plt.show()

