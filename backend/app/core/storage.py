from __future__ import annotations

import boto3
from botocore.exceptions import ClientError
from loguru import logger
from app.core.config import settings

class StorageService:
    """Handles file transfers directly to/from Cloudflare R2 bucket storage using S3 client API."""

    def __init__(self):
        self.bucket = settings.CLOUDFLARE_R2_BUCKET
        self.s3_client = None
        if settings.CLOUDFLARE_R2_ACCESS_KEY and settings.CLOUDFLARE_R2_SECRET_KEY:
            # R2 Endpoint URL format: https://<accountid>.r2.cloudflarestorage.com
            endpoint_url = f"https://{settings.CLOUDFLARE_ACCOUNT_ID}.r2.cloudflarestorage.com"
            self.s3_client = boto3.client(
                "s3",
                endpoint_url=endpoint_url,
                aws_access_key_id=settings.CLOUDFLARE_R2_ACCESS_KEY,
                aws_secret_access_key=settings.CLOUDFLARE_R2_SECRET_KEY,
            )

    async def upload_file(self, file_bytes: bytes, object_name: str) -> str:
        """Upload raw file content to the R2 bucket container."""
        if not self.s3_client:
            logger.warning("R2 Client not initialized. Returning mock path.")
            return f"https://mock-storage.interviewos.io/{object_name}"

        try:
            self.s3_client.put_object(
                Bucket=self.bucket,
                Key=object_name,
                Body=file_bytes,
            )
            return f"https://{self.bucket}.r2.cloudflarestorage.com/{object_name}"
        except ClientError as e:
            logger.error(f"Failed uploading file to R2: {e}")
            raise e
