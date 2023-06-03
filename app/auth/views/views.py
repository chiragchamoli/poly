from fastapi import APIRouter, Cookie, Request

router = APIRouter()

@router.get("/", name="Root")
def index():
    pass