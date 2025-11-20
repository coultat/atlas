from unittest.mock import MagicMock, patch

import pytest
from httpx import Response
from integration.conftest import artist_response

from atlas.apis.spotify.client import SpotifyClient
from atlas.models.spotify.config import SpotifyConfig


class TestSpotifyClientMocks:
    @patch("atlas.apis.base_api_client.AsyncClient.send")
    @pytest.mark.asyncio
    async def test_spotify_client_complete_flow(self, mock_send: MagicMock) -> None:
        # Sets up different responses for connect() and get_artist()
        mock_responses = [
            # First call: connect() - token
            MagicMock(
                spec=Response,
                status_code=200,
                json=MagicMock(
                    return_value={
                        "access_token": "mock_token_123",
                        "token_type": "Bearer",
                        "expires_in": 3600,
                    }
                ),
                raise_for_status=MagicMock(),
            ),
            # Second call: get_artist() - artist data
            MagicMock(
                spec=Response,
                status_code=200,
                json=MagicMock(return_value=artist_response()),
                raise_for_status=MagicMock(),
            ),
        ]
        mock_send.side_effect = mock_responses

        # Instances with fake credentials
        fake_credentials = SpotifyConfig(
            client_id="fake_client_id", secret="fake_secret"
        )
        client = SpotifyClient(fake_credentials)

        # test connect
        await client.connect()
        assert client.token == "mock_token_123"

        # Test get_artist()
        artist = await client.get_artist("1vCWHaC5f2uS3yhpwWbIA6")
        assert artist.name == "Avicii"

        # Amount of calls
        assert mock_send.call_count == 2
