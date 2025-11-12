from atlas.models.spotify.config import SpotifyConfig
from atlas.models.spotify.artist import Artist
from typing import Any
from functools import wraps

import httpx


class SpotifyClient:
    def __init__(self, credentials: SpotifyConfig) -> None:
        self.client_id = credentials.client_id
        self.secret = credentials.secret

    def _check_credentials(func) -> bool:
        @wraps(func)
        async def wrapper(self, *args, **kwargs):
            if not hasattr(self, "token"):
                await self.connect()
            return await func(self, *args, **kwargs)

        return wrapper

    def _get_base64_encoded_credentials(self) -> str:
        import base64

        credentials = f"{self.client_id}:{self.secret}"
        encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode(
            "utf-8"
        )
        return encoded_credentials

    async def connect(self) -> bool:
        encoded_credentials = self._get_base64_encoded_credentials()
        response = httpx.post(
            "https://accounts.spotify.com/api/token",
            data={"grant_type": "client_credentials"},
            headers={
                "Authorization": f"Basic {encoded_credentials}",
                "Content-Type": "application/x-www-form-urlencoded",
            },
        )
        response.raise_for_status()
        self.token = response.json().get("access_token")

    @_check_credentials
    async def get_artist(self, artist_id: str) -> Artist: # type: ignore # Todo change this after creating models
        result = httpx.get(
            f"https://api.spotify.com/v1/artists/{artist_id}",
            headers={"Authorization": f"Bearer {self.token}"},
        )
        result.raise_for_status()
        artist = Artist.model_validate(result.json())
        return artist
