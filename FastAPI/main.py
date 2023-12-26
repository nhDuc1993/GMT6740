from fastapi import FastAPI
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import joblib
import uvicorn

from model.indicator import Indicator

app = FastAPI()

origins = [
    'http://localhost:3000'
]

app.add_middleware(
        CORSMiddleware,
    allow_origins=origins, # Allows all origins
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods
    allow_headers=["*"], # Allows all headers
    )

preprocessing = joblib.load("./FastAPI/model/preprocessing.joblib")
linear_regression = joblib.load("./FastAPI/model/linear_regression.joblib")


@app.post("/submission")
async def read_submission(data: dict):
    df = pd.DataFrame([data], columns = ['maker', 'model', 'mileage', 'engine_displacement', 'engine_power',
       'body_type', 'transmission', 'door_count', 'seat_count', 'fuel_type',
       'man_period', 'stk_period'])
    cat_cols = [0,1,5,6,9]
    df.iloc[:,cat_cols] = df.iloc[:,cat_cols].fillna('unknown')

    arr = df.to_numpy()

    X_trans = preprocessing.transform(arr)
    y_pred = linear_regression.predict(X_trans)

    return round(y_pred[0],2)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)