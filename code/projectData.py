import numpy as np;

def projectData(X, U, K):


    U_reduce = U[:,:K].copy();

    Z = np.dot(X, U_reduce);

    return Z;
    
