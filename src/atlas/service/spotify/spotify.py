from atlas.apis.spotify.client import SpotifyClient
from atlas.models.spotify.artist import Artist


class SpotifyService:
    def __init__(self, client: SpotifyClient):
        self.client = client

    async def fetch_artist(self, artist_id: str) -> Artist:
        artist = await self.client.get_artist(artist_id)
        return artist
