from fastapi import FastAPI
from pydantic import BaseModel
import fastapi
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

print(fastapi.__version__)
print ("runing the python codes")
# Allow frontend (running in browser) to call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for prototype; later restrict to your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input schema
class CropInput(BaseModel):
    rain: float
    temp: float
    soil_index: int

@app.post("/predict")
def predict(input: CropInput):
    # Prototype rules
    soil = input.soil_index
    rain = input.rain
    temp = input.temp

    result = "Unknown"

    if soil == 2:  # Clay soil
        if rain < 300:
            result = "Yield < 8"
        elif 300 <= rain <= 350:
            result = "Yield between 9–11"
        elif rain > 400:
            result = "Yield > 12"
        else:
            result = "Yield uncertain"
    else:
        # Generic rule for non-clay soils (just an example)
        if rain < 250:
            result = "Low"
        elif 250 <= rain <= 400:
            result = "Medium"
        else:
            result = "High"

    return {"prediction": result}


