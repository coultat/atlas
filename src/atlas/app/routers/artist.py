from fastapi import APIRouter, Depends

from atlas.apis.base_api_client import BaseAPIClient
from atlas.dependencies.spotify import get_spotify_client
from atlas.models.spotify.artist import Artist
from atlas.service.spotify.spotify import SpotifyService

artist_router = APIRouter(prefix="/artist", tags=["artist"])

spotify_client = get_spotify_client()


@artist_router.get("/{artist_id}")
async def get_artist(
    artist_id: str,
    spotify_service: BaseAPIClient = Depends(lambda: SpotifyService(spotify_client)),
) -> Artist:
    artist = await spotify_service.fetch_artist(artist_id)
    return artist
