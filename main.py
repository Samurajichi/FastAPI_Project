"""Main module for the FastAPI application.

This module initializes the FastAPI app and defines API endpoints for the project.
"""
from fastapi import FastAPI
from mangum import Mangum
app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Mordo, chyba wszystk sie udalo"}

handler = Mangum(app=app)