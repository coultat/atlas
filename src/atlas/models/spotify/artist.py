from pydantic import BaseModel, ConfigDict, Field, HttpUrl


class ExternalUrls(BaseModel):
    spotify: HttpUrl


class Followers(BaseModel):
    model_config = ConfigDict(extra="forbid")
    href: str | None = Field(default=None)
    total: int = Field(default=0)


class Images(BaseModel):
    url: HttpUrl
    height: int
    width: int


class Artist(BaseModel):
    model_config = ConfigDict(
        extra="forbid", validate_by_name=True, validate_by_alias=True
    )
    external_urls: ExternalUrls
    followers: Followers
    genres: list[str]
    href: HttpUrl
    artist_id: str = Field(alias="id")
    images: list[Images]
    name: str
    popularity: int
    type_: str = Field(alias="type")
    uri: str
