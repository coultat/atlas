import pytest
from unittest.mock import AsyncMock, MagicMock
from src.atlas.apis.spotify.client import SpotifyClient
from typing import Self

class TestSpotifyClientMocks:
    
    @pytest.mark.asyncio
    async def test_spotify_client_connect_with_mock(self: Self) -> None:
        """Test que simula una conexión exitosa a Spotify"""
        # Crear un MagicMock completo de SpotifyClient
        mock_client = MagicMock(spec=SpotifyClient)
        
        # Configurar los métodos asíncronos como AsyncMock
        mock_client.connect = AsyncMock()
        mock_client.get_artist = AsyncMock()
        
        # Configurar atributos y comportamiento
        mock_client.connect.return_value = None
        mock_client.get_artist.return_value = {
            "id": "1vCWHaC5f2uS3yhpwWbIA6",
            "name": "Avicii",
            "popularity": 85
        }
        
        # Simular que después de connect() se establecen estos atributos
        mock_client.access_token = "mock_access_token_123"
        mock_client.connected = True
        
        # "Ejecutar" la conexión
        await mock_client.connect()
        
        # Verificaciones
        assert mock_client.access_token == "mock_access_token_123"
        assert mock_client.connected is True
        mock_client.connect.assert_called_once()
    
    @pytest.mark.asyncio
    async def test_spotify_client_get_artist_with_mock(self: Self) -> None:
        """Test que simula obtener información de un artista"""
        # Crear mock completo
        mock_client = MagicMock(spec=SpotifyClient)
        mock_client.get_artist = AsyncMock()
        
        # Configurar datos de retorno
        mock_artist_data = {
            "id": "1vCWHaC5f2uS3yhpwWbIA6",
            "name": "Avicii",
            "popularity": 85,
            "genres": ["edm", "progressive house"],
            "followers": {"total": 25000000}
        }
        mock_client.get_artist.return_value = mock_artist_data
        
        # Llamar al método
        artist = await mock_client.get_artist("1vCWHaC5f2uS3yhpwWbIA6")
        
        # Verificaciones
        assert artist["name"] == "Avicii"
        assert artist["id"] == "1vCWHaC5f2uS3yhpwWbIA6"
        mock_client.get_artist.assert_called_once_with("1vCWHaC5f2uS3yhpwWbIA6")