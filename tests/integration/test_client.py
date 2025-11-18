from src.atlas.apis.spotify.client import SpotifyConfig
from httpx import Response
import json
from unittest.mock import patch, MagicMock
import pytest
from atlas.apis.spotify.client import SpotifyClient
from tests.integration.conftest import artist_response


class TestSpotifyClientMocks:
    @patch("src.atlas.apis.base_api_client.AsyncClient.send")
    @pytest.mark.asyncio
    async def test_spotify_client_complete_flow(self, mock_send):
        # Configurar diferentes respuestas para diferentes llamadas
        mock_responses = [
            # Primera llamada: connect() - token
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
            # Segunda llamada: get_artist() - datos artista
            MagicMock(
                spec=Response,
                status_code=200,
                json=MagicMock(return_value=artist_response()),
                raise_for_status=MagicMock(),
            ),
        ]
        mock_send.side_effect = mock_responses

        # Crear instancia REAL con credenciales falsas
        fake_credentials = SpotifyConfig(
            client_id="fake_client_id", secret="fake_secret"
        )
        client = SpotifyClient(fake_credentials)

        # Probar connect()
        await client.connect()
        assert client.token == "mock_token_123"

        # Probar get_artist()
        artist = await client.get_artist("1vCWHaC5f2uS3yhpwWbIA6")
        assert artist.name == "Avicii"

        # Verificar llamadas
        assert mock_send.call_count == 2
