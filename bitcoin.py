import math
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data=pd.read_csv("bitcoin_archive_data.csv")

data = data[['Price','Open','High','Low']]
data['label']=data['Price'].shift(7)

X=np.array(data[['Open','High','Low']])
y= np.array(data["Price"])

X_last=X[:7]
X=X[7:]
y=y[7:]


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

clf=LinearRegression()
clf.fit(X_train,y_train)

confidence=clf.score(X_test,y_test)
confidence

forecast=clf.predict(X_last)
forecast
