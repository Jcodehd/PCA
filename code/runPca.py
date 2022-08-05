import numpy as np;


def runPca(X):

    m = X.shape[0];

    sigma = np.dot(X.T, X)/m;
    
    U, S, V = np.linalg.svd(sigma);



    return U, S;

    

