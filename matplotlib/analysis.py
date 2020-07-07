import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#resize the graph
plt.figure(figsize=(5,4))

x=[0,1,2,3,4,5]
y=[0,2,4,6,8,10]
x2=np.arange(0,4.5,0.5)
plt.plot(x2,x2**2, label='x2^2',marker='.', markersize=10, linestyle='--')
plt.plot(x2, label='x2',marker='.', markersize=10, linestyle='--')
plt.plot(x,y, label='x/y', color='#000000', linewidth=3, marker='.', markersize=10, markeredgecolor='blue', linestyle='--')
# plt.plot(x,y, label='x',marker='.', markersize=10, linestyle='--')

#print the legend
plt.legend()

plt.title('First graph', fontdict={'fontname':'Comic Sans MS'})
plt.xlabel("Abcisses", fontdict={'fontname':'Comic Sans MS'})
plt.ylabel("Ordonnées", fontdict={'fontname':'Comic Sans MS'})

#save
# plt.savefit('mygraph.png',dpi=300)

#print(the graph)
# plt.show()


# labels=['A','B','C']
# values=[1,4,2]
# plt.bar(labels,values)
plt.show()