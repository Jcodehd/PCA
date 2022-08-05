from certifi import where
import numpy as np;

def chooseK(S):

    m = len(S);
    S_sum = np.sum(S);
    K = 1;
    while(True):

        t = np.sum(S[:K])/S_sum;

        if t >= 0.99:
            break;
        
        K = K+1;

    return K;



