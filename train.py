import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle
import mlflow

data = pd.DataFrame({
    "age": [22,25,47,52,46,56],
    "salary": [20000,25000,50000,60000,52000,65000],
    "buy": [0,0,1,1,1,1]
})

x=data[['age','salary']]
y=data['buy']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,stratify=y)

with mlflow.start_run():
    model=LogisticRegression()
    model.fit(x_train,y_train)

    acc=model.score(x_test,y_test)
    mlflow.log_metric("accuracy",acc)

    with open("modelbasic.pkl","wb") as f:
        pickle.dump(model,f)

print("model trained and saved")
