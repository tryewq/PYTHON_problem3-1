import numpy as np
import matplotlib.pyplot as plt

mp=np.arange(0,100);

for i in range(0,100):
 if mp[i]<=9:
   mp[i] = ((mp[i]**2)-7)
   
 elif mp[i]>=10:
     mp[i] = mp[i-10]
     
     plt.stem(mp,use_line_collection=True)
     plt.xlabel("n = 0 to = 99")
     plt.ylabel("f(n)")
     plt.title('Graph of the function')
     
     plt.figure()
     plt.show()