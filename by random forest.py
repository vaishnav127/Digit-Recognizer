
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

train_url="C:/Users/dell/Desktop/train.csv"
train=pd.read_csv(train_url)

test_url="C:/Users/dell/Desktop/test.csv"
test=pd.read_csv(test_url)

target=train["label"]
t=train.iloc[:,1:].values
X_train=t
X_test=test


model=RandomForestClassifier(n_estimators=100)
#check from here
model=model.fit(X_train,target)

prediction=model.predict(X_test)

image_number=np.arange(1,28001)

data={'ImageId':image_number,                
      'Label':prediction
}
solution=pd.DataFrame(data)
solution.to_csv("C:/Users/dell/Desktop/digit.csv",index=False)








