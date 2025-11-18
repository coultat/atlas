from abc import ABC, abstractmethod
from typing import Any

from httpx import AsyncClient, ConnectError, ConnectTimeout, HTTPStatusError

MAX_RETRIES = 3


class BaseAPIClient(ABC):
    async def _request(
        self,
        verb: str,
        url: str,
        headers: dict[str, str] | None,
        data: dict[str, str] | None = None,
        timeout: float = 15.00,
    ) -> Any:
        async with AsyncClient() as client:
            for i in range(MAX_RETRIES):  # Retry logic
                try:
                    request = client.build_request(
                        verb, url, headers=headers, data=data, timeout=timeout
                    )
                    result = await client.send(request)
                    result.raise_for_status()
                    return result
                except ConnectTimeout:
                    if i == MAX_RETRIES - 1:
                        raise ConnectTimeout("Max retries exceeded")
                    timeout = timeout * 2.00
                except ConnectError as err:
                    raise ConnectError(f"Connection error occurred {err=}")
                except HTTPStatusError as http_err:
                    raise HTTPStatusError(
                        message=f"HTTP error occurred: {http_err=}",
                        request=http_err.request,
                        response=http_err.response,
                    )

    @abstractmethod
    async def connect(
        self, token_url: str, data: dict[str, str], headers: dict[str, str]
    ) -> Any:
        raise NotImplementedError
