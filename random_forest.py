# coding: utf-8
from sklearn.ensemble import RandomForestClassifier
# the random forest classifier uses an ensemble of
# decision trees. each tree is trained on a subset
# of the independent variables and their outputs are
# averaged together to arrive at the random forest's 
# prediction.
# the goal of this approach is to ameliorate the tendency
# of decision trees to overfit on training data
rf = RandomForestClassifier()

y = dat.Churn
X = dat.drop(['Churn', 'Phone', 'State'], axis=1) # remove our non-numeric data and the dependent variable

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=.25)
rf.fit(x_train, y_train)
accuracy_score(y_test, rf.predict(x_test))
