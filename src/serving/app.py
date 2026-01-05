from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI(title="ML Serving API", version="1.0.0")

# Dummy Model for demonstration
# In real scenario, load via: model = pickle.load(open("model.pkl", "rb"))
class DummyModel:
    def predict(self, data):
        return [0] * len(data)

model = DummyModel()

class InputData(BaseModel):
    features: list[float]

@app.get("/")
def home():
    return {"status": "healthy", "model_version": "v1"}

@app.post("/predict")
def predict(data: InputData):
    # Preprocessing
    input_array = np.array([data.features])
    
    # Prediction
    prediction = model.predict(input_array)
    
    return {"prediction": int(prediction[0])}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
