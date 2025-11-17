from enum import StrEnum


class SpotifyAPIEndpoint(StrEnum):
    ARTIST = "artists"


class SpotifyURL(StrEnum):
    TOKEN_URL = "https://accounts.spotify.com/api/token"
    BASE_API_URL = "https://api.spotify.com/v1/"
