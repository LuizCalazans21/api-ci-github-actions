from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "API online"}

@app.get("/somar/{a}/{b}")
def somar(a: int, b: int):
    # ERRO INTENCIONAL: trocado + por -
    return {"resultado": a - b}  