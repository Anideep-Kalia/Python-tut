from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello API!"}

@app.post("/predict")
def predict(age: int, fare: float, sex: str):
    return {"prediction": "Survived" if fare > 20 else "Did not survive"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


# uvicorn app:app --reload       => top run the backend server
