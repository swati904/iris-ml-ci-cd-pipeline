import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

#load data
data=pd.read_csv('data/iris.csv')

#preprocessing
x=data.drop('species', axis=1)
|y=data['species']

#splitting data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2, random_state=42)



#loadind the saved model
model=joblib.load('model/iris_model.pkl')

#make prediction
y_pred=model.predict(x_test)

#evaluating
accuracy=accuracy_score(y_test,y_pred)
print(f'model accuracy:{accuracy:.2f}')