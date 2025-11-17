from functools import wraps
from typing import Any, Callable, Self

from atlas.apis.base_api_client import BaseAPIClient
from atlas.models.spotify.artist import Artist
from atlas.models.spotify.config import SpotifyConfig
from atlas.models.spotify.urls import SpotifyAPIEndpoint, SpotifyURL


class SpotifyClient(BaseAPIClient):
    def __init__(self, credentials: SpotifyConfig) -> None:
        self.client_id = credentials.client_id
        self.secret = credentials.secret

    def _check_credentials(func: Callable[..., Any]) -> Any:
        @wraps(func)
        async def wrapper(self: Self, *args: Any, **kwargs: Any) -> Any:
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

    async def connect(self) -> None:
        encoded_credentials = self._get_base64_encoded_credentials()
        url = SpotifyURL.TOKEN_URL
        headers = {
            "Authorization": f"Basic {encoded_credentials}",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {"grant_type": "client_credentials"}
        response = await self._request(
            "POST",
            url=url,
            data=data,
            headers=headers,
        )
        if response.json().get("access_token") is None:
            raise ValueError("Failed to obtain access token from Spotify")
        self.token = response.json()["access_token"]

    @_check_credentials
    async def get_artist(self, artist_id: str) -> Artist:
        url = f"{SpotifyURL.BASE_API_URL}{SpotifyAPIEndpoint.ARTIST}/{artist_id}"
        headers = {"Authorization": f"Bearer {self.token}"}
        result = await self._request("GET", url, headers=headers)
        artist = Artist.model_validate(result.json())
        return artist
