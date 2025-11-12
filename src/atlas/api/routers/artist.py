from fastapi import APIRouter, Depends
from functools import lru_cache
from atlas.dependencies.spotify import get_spotify_client
from atlas.spotify.client import SpotifyClient
from atlas.models.spotify.artist import Artist


artist_router = APIRouter(prefix="/artist", tags=["artist"])



@artist_router.get("/{artist_id}")
async def get_artist(artist_id: str,
                     spotify_client: SpotifyClient = Depends(get_spotify_client)) -> Artist: # type: ignore # Todo change this after creatin models
    artist = await spotify_client.get_artist(artist_id)
    return artist


