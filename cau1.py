import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier


data = pd.read_excel('cau1.xlsx',encoding='utf-8')


data_target = data.iloc[:,0] 
print(data_target)

data_train=data.iloc[:,1:61]
print(data_train)

tree=DecisionTreeClassifier()
model_tree=tree.fit(data_train,data_target)

data_predict=pd.read_excel('cau1_predict.xlsx',encoding='utf-8')


result = model_tree.predict(data_predict)

print(result)

