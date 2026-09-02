#Integration testing + functional test 

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import numpy as np


def pipeline(x,y):    # x: features, y : target 
    #Step -1 : Preprossing the data 
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)

    #Step -2 : Model training 

    model = LogisticRegression()
    model.fit(x_scaled, y)
    return model, scaler 

#integartion test function 
def test_pipeline():
    x= np.array([[1,2],[3,4],[5,6]])
    y=[0,1,0]
    model ,scaler =pipeline(x,y)


    x_transfromed =scaler.transform(x)

    preds = model.predict(x_transfromed)
    #checking every value in the prediction and verify that is either 0 or 1
    assert all(p in [0,1] for p in preds )