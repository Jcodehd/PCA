import scipy.io as sc
import numpy as np;
from featureNormalize import featureNormalize;
from runPca import runPca;
from chooseK import chooseK;
from projectData import projectData;

# 加载数据
data = sc.loadmat('Machine Learning/PCA/ex7faces.mat');
X = data['X'];

# 均值归一化
X_norm, aver_, std_ = featureNormalize(X);

# PCA
U, S= runPca(X_norm);

# 获取保存了百分之99方差的维度
K = chooseK(S);

# 降维
Z = projectData(X_norm, U, K);
















