from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
async def test():
    return {"message": "OK!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
