from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def main():
    return "hello from fast api"