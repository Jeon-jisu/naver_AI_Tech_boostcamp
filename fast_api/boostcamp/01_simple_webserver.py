from fast_api import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
