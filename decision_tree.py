# coding: utf-8

import pandas as pd
dat = pd.read_excel('./Customer_Telecom_Churn.xls')
from sklearn.tree import DecisionTreeClassifier
y = dat.Churn
dat.columns
X = dat[['CustServ Calls', 'Account Length', 'Day Mins']]
t = DecisionTreeClassifier()
help(t.fit)
t.fit(X, y)
from sklearn.metrics import accuracy_score
accuracy_score(y, t.predict(X))
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=.25, random_state=0)
t_r = DecisionTreeClassifier()
t_r.fit(x_train, y_train)
t_r.predict(x_test).abs().mean()
t_r.predict(x_test)..mean()
t_r.predict(x_test).mean()
t_r.predict(x_test).count_values()
t_r.predict(x_test)
accuracy_score(y_test, t_r.predict(x_test))
help(train_test_split)
# use more data to make our decisions
X = dat.drop(['Churn', 'Phone', 'State'], axis=1)
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=.25, random_state=0)
t_rr = DecisionTreeClassifier()
t_rr.fit(x_train, y_train)
accuracy_score(y_test, t_rr.predict(x_test))
help(train_test_split)
