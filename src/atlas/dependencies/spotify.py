from atlas.models.spotify.config import SpotifyConfig, get_spotify_config
from functools import lru_cache
from atlas.spotify.client import SpotifyClient

@lru_cache
def get_spotify_config_cached() -> SpotifyConfig:
    return SpotifyConfig()

def get_spotify_client() -> SpotifyClient:
    return SpotifyClient(get_spotify_config_cached())