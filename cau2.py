import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier


data = pd.read_excel('cau2_train.xlsx',encoding='utf-8')

data_target = data.iloc[:,0] 
print(data_target)

data_train=data.iloc[:,1:61]
print(data_train)

tree=DecisionTreeClassifier()
model_tree=tree.fit(data_train,data_target)

data_predict=pd.read_excel('cau2_predict.xlsx',encoding='utf-8')

data_result=pd.read_excel('cau2_result.xlsx',encoding='utf-8')


result=model_tree.predict(data_predict)

data_result['predict'] = result

writer = pd.ExcelWriter('cau2_predict&result.xlsx', engine='xlsxwriter')

data_result.to_excel(writer, sheet_name='Sheet1', index=False)

writer.save()




