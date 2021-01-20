import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold

data = pd.read_excel('cau1.xlsx',encoding='utf-8')

train, test = train_test_split(data, test_size=0.3)

#train, test = train_test_split(data, test_size=0.4)
#train, test = train_test_split(data, test_size=0.3,shuffle=False)

print(train)
print(test)


