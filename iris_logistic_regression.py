import sklearn
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
#print(sklearn.__version__)
#read data
iris=datasets.load_iris()
#print(iris.feature_names)

#print(iris.target_names)
#spilt data into train and test sets
X=iris.data
y=iris.target
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.3)
#print(X_train.shape)

#build and train model
#using supervised learning ie decision trees
#classifier = LogisticRegression()
classifier = RandomForestClassifier()
classifier.fit(X_train,y_train)

#make predictions/Evaluate

predictions = classifier.predict(X_test)
accuracy = accuracy_score(y_test,predictions)
print("accuracy score is: ",accuracy) 