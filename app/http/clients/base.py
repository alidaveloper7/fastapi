from __future__ import annotations
import httpx
from typing import Any, Optional

class BaseHttpClient:
    def __init__(self, base_url: str, token: Optional[str] = None, timeout: float = 10.0):
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.timeout = timeout

    def _headers(self) -> dict[str, str]:
        h = {"Content-Type": "application/json"}
        if self.token:
            h["Authorization"] = f"Bearer {self.token}"
        return h

    async def post_json(self, path: str, data: dict[str, Any]) -> httpx.Response:
        url = self.base_url + path
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            resp = await client.post(url, headers=self._headers(), json=data)
            resp.raise_for_status()
            return resp
