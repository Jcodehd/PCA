import numpy as np

# 归一化
def featureNormalize(data):

    m = data.shape[0];


    aver_ = np.mat(np.mean(data, axis=0)); # 平均值

    std_  = np.mat(np.std(data, axis=0)); # 标准差
    


    #归一化
    data = (data - np.repeat(aver_, m, axis=0))/np.repeat(std_, m, axis=0);
    # repeat 复制行列 axis为0时复制行 为1时复制列

    return data, aver_, std_;