from fastapi import FastAPI
from users.controller import router as users_router

app = FastAPI()
# handler = Mangum(app=app)

@app.get('/')
async def root():
    return {"message": "Mordo, chyba wszystk sie udalo"}


def register_routes(app: FastAPI):  
    app.include_router(users_router)



register_routes(app)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)