"""Main module for the FastAPI application.

This module initializes the FastAPI app and defines API endpoints for the project.
"""
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def main():
    return "hello from fast api"
