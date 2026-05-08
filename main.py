from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "API online"}

@app.get("/somar/{a}/{b}")
def somar(a: int, b: int):
    return {"resultado": a + b}

@app.get("/multiplicar/{a}/{b}")
def multiplicar(a: int, b: int):
    return {"resultado": a * b}