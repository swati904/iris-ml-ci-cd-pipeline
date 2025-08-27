import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

#load data
data=pd.read_csv('data/iris.csv')
reprocessing

x=data.drop('species', axis=1)
|y=data['species']

#splitting data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2, random_state=42)
#training model
model=RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(x_train, y_train)

#saving model
joblib.dump(model, 'model/iris_model.pkl')