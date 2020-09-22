#-*- coding:utf-8 -*-

# 使用R
import rpy2.robjects as robjects
import pandas as pd
import  re
import os
import pathlib
import numpy as np
from sklearn.utils import shuffle
from rpy2.robjects.packages import importr
rnalytica = importr('Rnalytica')
from rpy2.robjects import pandas2ri
pandas2ri.activate()
from imblearn.over_sampling import BorderlineSMOTE

# 基于Spearman特征选择 获得metric名称及数据
def getAutoSpearmanMetric(path):
    data = pd.read_csv(path)
    robjects.globalenv['data'] = data
    indep = robjects.r.colnames(data)
    res = str(rnalytica.AutoSpearman(dataset = data,  metrics = indep))
    # 提取metric的名称
    metric_res = re.findall(r'"([\S\s]+?)"',res)
    # 获取相应的数据
    metric_res_data = data.ix[:,metric_res]
    return metric_res,metric_res_data

# 返回特征选择的所有版本的metric 并生成训练集
def create_metric(soft,metric,release,fold=3,boderlinesmote=False):
    all = []
    for i in range(release):
        path = 'F:\\orca-master\\exampledata\\mData\\ordinalRegressionData\\Three severity\\'+metric+'\\'+soft+'\\'+str(i+1)+'_code&network_metrics&bugs.csv'
        auto_spearman_metric,auto_spearman_metric_data = getAutoSpearmanMetric(path)
        all.append(auto_spearman_metric)
        for k in range(fold):
            if boderlinesmote:
                # 使用borderlinSMOTE
                auto_spearman_metric_data=auto_spearman_metric_data.dropna(axis=1)
                x = auto_spearman_metric_data.iloc[:,0:-1]
                y = auto_spearman_metric_data.iloc[:,-1:]

                bord_smote = BorderlineSMOTE(random_state=16,kind="borderline-1")
                x_res,y_res = bord_smote.fit_resample(x,y)
                auto_spearman_metric_data =pd.merge(x_res,y_res,how='left',left_index =  True,right_index = True)
            save_path= 'F:\\orca-master\\exampledata\\'+metric+'\\'+soft+'\\'+str(fold)+'-fold\\'+soft+str(i+1)+'\\matlab\\'+'train_'+soft+str(i+1)+'.'+str(k)
            tmp = shuffle(auto_spearman_metric_data)
            tmp.to_csv(save_path, header=None, index=False, sep=" ")
    return all

	