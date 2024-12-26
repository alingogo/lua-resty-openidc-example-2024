"""Endpoints module."""

from typing import Optional, List

from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel
from dependency_injector.wiring import inject, Provide

from services import MyService
from containers import Container

from jose import jwt


class Response(BaseModel):
    who: str

router = APIRouter()

@router.get("/", response_model=Response)
@inject
async def index(
        request: Request,
        my_service: MyService = Depends(Provide[Container.my_service]),
):
    token = request.headers["x-oidc-token"]
    print(token)

    secret_key = "secret_key_200a9737bfc6d55b37085f0589f"
    ALGORITHM = "HS256"
    payload = jwt.decode(token, secret_key, algorithms=[ALGORITHM])
    print(dict(payload))

    res = await my_service.name()
    return {
        "who": res,
    }