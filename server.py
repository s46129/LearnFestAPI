from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI()

class MessageStruct(BaseModel):
    message: str

@app.get("/test")
async def test():
    return {"message": "OK!"}

@app.post("/testPostMessageStruct")
async def testPostMessageStruct(message:MessageStruct):
    return {"message": "Received: " + message.message}

@app.post("/testPost")
async def testPost(data: Dict[str, Any]):
    return {"received_data": data}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
