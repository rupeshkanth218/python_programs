from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import csv

features=[]
outcomes=[]
with open('IRIS.csv','r') as file:
    data=csv.reader(file)
    for i in data:
        features.append(i[0:4])
        outcomes.append(i[4])
features.pop(0)
outcomes.pop(0)
outcomes=list(map(lambda species: 0 if species =='Iris-setosa' else(1 if species =='Iris-versicolor' else 2),outcomes))
testing_features=[]
testing_outcomes=[]
train_features=[]
train_outcomes=[]

train_features, testing_features, train_outcomes, testing_outcomes = train_test_split(features, outcomes, test_size=0.10, random_state=42)
#if we dont use test_train_split function
"""
for i in range(3):
    testing_features.append(features.pop(47))
    testing_outcomes.append(outcomes.pop(47))
for i in range(3):
    testing_features.append(features.pop(94))
    testing_outcomes.append(outcomes.pop(94))
for i in range(3):
    testing_features.append(features.pop(141))
    testing_outcomes.append(outcomes.pop(141))
print(outcomes)"""
dtc=DecisionTreeClassifier()
dtc.fit(train_features,train_outcomes)
y_predict=dtc.predict(testing_features)
print(accuracy_score(testing_outcomes,y_predict))
