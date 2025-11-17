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
