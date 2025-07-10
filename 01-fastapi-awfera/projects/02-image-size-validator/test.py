from typing import Annotated

from fastapi import FastAPI, File, UploadFile

import uvicorn

app = FastAPI()

@app.get("/")
async def read_route():
    return "Hello"


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    length = len(file)
    response = "Valid File" if length < 2 * 1024 * 1024 else "File is too large"
    return response

if __name__ == "__main__":
    uvicorn.run(app="test:app", host="127.0.0.1" ,port=800, reload=True)