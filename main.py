from fastapi import FastAPI
from mangum import Mangum
from users.controller import router as users_router

app = FastAPI()
handler = Mangum(app=app)

@app.get('/')
async def root():
    return {"message": "Mordo, chyba wszystk sie udalo"}


def register_routes(app: FastAPI):  
    app.include_router(users_router)



register_routes(app)


