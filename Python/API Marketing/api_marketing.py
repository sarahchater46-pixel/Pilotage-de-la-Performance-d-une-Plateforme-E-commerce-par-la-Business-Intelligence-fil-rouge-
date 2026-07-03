from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

df = pd.read_csv("fait_marketing.csv")

@app.get("/api/v1/marketing")
def get_marketing_data(limit: int = 100):
    return {
        "status": "success",
        "total_records": len(df),
        "data": df.head(limit).to_dict(orient="records")
    }