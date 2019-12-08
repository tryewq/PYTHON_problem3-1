import numpy as np
import math

display("Enter a nx2 matrix:")

def least3(e):
    x = e[:,0];
    y = e[:,1];

    l = len(x);
    
    for n in range(0,9): 
        if n>=l:
            break
        
        fit = np.polyfit(x,y,n) 
        f = np.polyval(fit,x) 
        
        #formula for least norm error
        m = y-f 
        error = np.linalg.norm(m)
        
    print('Coefficients of the polynomial: ',fit) 

