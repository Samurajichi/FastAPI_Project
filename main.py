"""Main module for the FastAPI application.

This module initializes the FastAPI app and defines API endpoints for the project.
"""
from fastapi import FastAPI
from mangum import Mangum
app = FastAPI()

@app.get('/')
def get_all():
    """Take a number n and return the square of n."""
    return {"message": "hello from Erkner"}

handler = Mangum(app=app)