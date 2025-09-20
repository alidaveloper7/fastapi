from __future__ import annotations
from typing import Optional
from app.http.clients.base import BaseHttpClient

class EmailHttpClient(BaseHttpClient):
    def __init__(self, base_url: str, send_path: str, token: Optional[str] = None):
        super().__init__(base_url=base_url, token=token)
        self.send_path = send_path

    async def send_email(self, to: str, subject: str, body: str) -> None:
        payload = {"to": to, "subject": subject, "body": body}
        await self.post_json(self.send_path, payload)
