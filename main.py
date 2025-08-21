"""Main module for the FastAPI application.

This module initializes the FastAPI app and defines API endpoints for the project.
"""
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def get_all():
    """Take a number n and return the square of n."""
    return "hello from fast api"
