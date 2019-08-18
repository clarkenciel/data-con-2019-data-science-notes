# coding: utf-8
import sklearn
from sklearn.tree import DecisionTreeClassifier
t = DecisionTreeClassifier()
t.fit(X, y)
help
# predict whether someone with one customer service call,
# 90 months of service and 100 daytime minutes of usage
# will leave
t.predict([[1, 90, 100]])
# predict whether someone with 4 customer service calls,
# 25 months of service and 100 daytime minutes of usage
# will leave
t.predict([[4, 25, 100]])
