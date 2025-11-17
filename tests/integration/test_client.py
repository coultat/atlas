from unittest.mock import AsyncMock, Mock, patch

import httpx
import pytest
from fastapi.testclient import TestClient
from pytest_httpx import HTTPXMock

from atlas.apis.spotify.client import SpotifyClient
from atlas.app.app import app
from atlas.models.spotify.urls import SpotifyURL
from tests.integration.conftest import MockSpotifyConfig

client = TestClient(app)


@pytest.mark.asyncio
async def test_spotify_client_connect(mock_credentials: MockSpotifyConfig) -> None:
    # Mock of the response for the Spotify token endpoint
    mock_response = Mock(spec=httpx.Response)
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "access_token": "mock_token_123",
        "token_type": "bearer",
        "expires_in": 3600,
    }
    mock_response.raise_for_status.return_value = None

    with patch(
        "atlas.apis.base_api_client.AsyncClient.send", return_value=mock_response
    ):
        client = SpotifyClient(mock_credentials)
        await client.connect()

        assert client.token == "mock_token_123"
        assert hasattr(client, "token")


@pytest.mark.asyncio
async def test_spotify_client_connect_with_httpx_mock(
    httpx_mock: HTTPXMock, mock_credentials: MockSpotifyConfig
) -> None:
    """Test usando pytest-httpx (más limpio)"""
    # Mock del endpoint de token de Spotify
    httpx_mock.add_response(
        method="POST",
        url=SpotifyURL.TOKEN_URL,
        json={
            "access_token": "mock_token_456",
            "token_type": "bearer",
            "expires_in": 3600,
        },
        status_code=200,
    )

    client = SpotifyClient(mock_credentials)
    await client.connect()

    assert client.token == "mock_token_456"


def test_artist_endpoint_integration() -> None:
    """Integration test for /artist/{artist_id} endpoint"""
    with patch("atlas.apis.spotify.client.SpotifyClient") as MockSpotifyClient:
        mock_instance = MockSpotifyClient.return_value

        # Mock of the connect method (async)
        mock_instance.connect = AsyncMock()

        # Mocks artist method async
        mock_instance.get_artist = AsyncMock(
            return_value={
                "id": "1vCWHaC5f2uS3yhpwWbIA6",
                "name": "Avicii",
                "genres": ["electronic", "dance"],
                "popularity": 85,
            }
        )

        response = client.get("/artist/1vCWHaC5f2uS3yhpwWbIA6")

        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "Avicii"
        assert data["id"] == "1vCWHaC5f2uS3yhpwWbIA6"
