from fastapi import FastAPI
import uvicorn

app = FastAPI(
    description="Basic FastAPI",
    version="0.116.0"
)

@app.get("/")
def home():
    return {"message":"Hello from fastapi"}

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
