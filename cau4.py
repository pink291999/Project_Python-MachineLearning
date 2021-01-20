import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC 
from sklearn.metrics import accuracy_score


data = pd.read_excel('cau2_train.xlsx',encoding='utf-8')

data_target = data.iloc[:,0] 
print(data_target)

data_train=data.iloc[:,1:61]
print(data_train)

tree=DecisionTreeClassifier()
model_tree=tree.fit(data_train,data_target)

svm = SVC(gamma='auto')
model_svm = svm.fit(data_train, data_target)

data_predict=pd.read_excel('cau2_predict.xlsx',encoding='utf-8')

data_result=pd.read_excel('cau2_result.xlsx',encoding='utf-8')

result_tree=model_tree.predict(data_predict)
result_svm=model_svm.predict(data_predict)

x=accuracy_score(data_result,result_tree)
y=accuracy_score(data_result,result_svm)

print(x,y)

data_result['tree'] = result_tree
data_result['svm'] = result_svm

data_result.to_excel('cau4_predict&result.xlsx',index=0)




