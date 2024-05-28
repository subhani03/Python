import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([0,3,5])
ypoints=np.array([25,125,45])
font1={'family':'serif','color':'blue','size':'20'}
font2={'family':'serif','color':'pink','size':'20'}
plt.plot(xpoints,ypoints)
plt.title("matplot")
plt.xlabel("x-axis",fontdict=font1)
plt.plot(ypoints,marker='*')                                             
plt.ylabel("y_axis",fontdict=font2)


plt.show()