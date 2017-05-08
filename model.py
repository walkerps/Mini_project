import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import linear_model
from sklearn.neighbors import KDTree
from sklearn import tree
import pickle
file = 'Training_data.csv'

df = pd.read_csv(file)

Y = df['Sum'].values

df = df.drop(['Sum'],axis = 1)

X = df.values

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,train_size = 0.8)

model = svm.SVR(kernel = 'poly')

model.fit(X_train,Y_train)

filename = 'dataModel.sav'

pickle.dump(model,open(filename,'wb'))

