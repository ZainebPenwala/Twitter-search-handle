## predict price of stock 3 days in future
DATA SET = {features (01-H1-L1=C1) - label (C4)}
*** here we use liner regression algo y=mx+c
import math
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression

data=pd.read_csv('infy.csv')
print(data)
data=data[['Open Price','High Price','Low Price','Close Price']]
print(data)

** shift function is used to shift rows above as required .here we have to shift by -3 above. Shift rows above use (-) and shift rows below(+)
data['label']=data['Close Price'].shift(-3)
print(data)

** here X is features and x label
X=np.array(data.drop(['Close Price','label'],axis=1))
Or {X=np.array(data[['Open Price','High Price','Low Price']])}
Print(X)
print(X.shape)                            ## .shape gives dimensions 

X_lately=X[-3:]        ## these values contain NAN
X=X[:-3]
print(X_lately)


y=np.array(data['label'])
y=y[:-3]
print(y)
print(X.shape)
print(y.shape)

**train_test_split is used to divide the data into training and testing set by user defined ratio .it takes 3 parameters(x,y,ratio)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

clf=LinearRegression()                        ## clf is the object of class linear regression
**fit() func is a func inside linear regression class that will train the model 
**Score() func gives coefficient of determination
**predict() func takes the input and returns the output
clf.fit(X_train,y_train)
confidence=clf.score(X_test,y_test)
print(confidence)
forecast_set=clf.predict(X_lately)
print(forecast_set)
