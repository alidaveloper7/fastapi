from __future__ import annotations
from app.http.clients.email_client import EmailHttpClient

class EmailService:
    def __init__(self, client: EmailHttpClient):
        self.client = client

    async def send_welcome(self, to: str) -> None:
        await self.client.send_email(
            to=to,
            subject="Welcome!",
            body="Welcome to our platform!",
        )
