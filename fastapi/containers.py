"""Containers module."""
import os
from dependency_injector import containers, providers

from services import MyService
from settings import settings
from s3 import S3
from minio import Minio


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=["endpoints"])

    if settings.PLATFORM == "cloud":
        storage_client = providers.Singleton(
            S3
        )
        my_service = providers.Factory(
            MyService,
            storage_client=storage_client,
        )
    else: #onpre
        storage_client = providers.Singleton(
            Minio
        )
        my_service = providers.Factory(
            MyService,
            storage_client=storage_client,
        )