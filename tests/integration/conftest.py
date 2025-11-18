from typing import Self

import pytest


# Mock credentials for SpotifyClient
class MockSpotifyConfig:
    def __init__(self: Self) -> None:
        self.client_id = "mock_client_id"
        self.secret = "mock_secret"


@pytest.fixture
def mock_credentials() -> MockSpotifyConfig:
    return MockSpotifyConfig()


def artist_response() -> dict:
    return{
  "external_urls": {
    "spotify": "https://open.spotify.com/artist/1vCWHaC5f2uS3yhpwWbIA6"
  },
  "followers": {
    "href": None,
    "total": 23450757
  },
  "genres": [
    "edm"
  ],
  "href": "https://api.spotify.com/v1/artists/1vCWHaC5f2uS3yhpwWbIA6",
  "id": "1vCWHaC5f2uS3yhpwWbIA6",
  "images": [
    {
      "url": "https://i.scdn.co/image/ab6761610000e5ebae07171f989fb39736674113",
      "height": 640,
      "width": 640
    },
    {
      "url": "https://i.scdn.co/image/ab67616100005174ae07171f989fb39736674113",
      "height": 320,
      "width": 320
    },
    {
      "url": "https://i.scdn.co/image/ab6761610000f178ae07171f989fb39736674113",
      "height": 160,
      "width": 160
    }
  ],
  "name": "Avicii",
  "popularity": 80,
  "type": "artist",
  "uri": "spotify:artist:1vCWHaC5f2uS3yhpwWbIA6"
}