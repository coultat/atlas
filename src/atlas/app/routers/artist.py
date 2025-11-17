from fastapi import APIRouter, Depends

from atlas.apis.spotify.client import SpotifyClient
from atlas.dependencies.spotify import get_spotify_client
from atlas.models.spotify.artist import Artist

artist_router = APIRouter(prefix="/artist", tags=["artist"])


@artist_router.get("/{artist_id}")
async def get_artist(
    artist_id: str, spotify_client: SpotifyClient = Depends(get_spotify_client)
) -> Artist:
    artist = await spotify_client.get_artist(artist_id)
    return artist
