import datetime

from pydantic import BaseModel, field_validator


class AuthPrincipal(BaseModel):
    sub_merchant_id: int

class Token(BaseModel):
    token: str
    token_type: str
    expires_at: datetime.datetime
    sub_merchant_id: int
    auth_principal: AuthPrincipal


class TokenData(BaseModel):
    email: str | None = None

class TokenIn(BaseModel):
    access_key: str
    access_secret: str
    order_id: str | None = None

    @field_validator("access_key")
    @classmethod
    def access_key_is_not_blank(cls, value):
        if not value:
            raise ValueError("Access Key field can't be blank!")
        return value

    @field_validator("access_secret")
    @classmethod
    def access_secret_is_not_blank(cls, value):
        if not value:
            raise ValueError("Access Secret field can't be blank!")
        return value
