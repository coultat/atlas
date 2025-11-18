from functools import lru_cache

from atlas.apis.spotify.client import SpotifyClient
from atlas.models.spotify.config import SpotifyConfig


@lru_cache
def get_spotify_config_cached() -> SpotifyConfig:
    return SpotifyConfig()


def get_spotify_client() -> SpotifyClient:
    return SpotifyClient(get_spotify_config_cached())
