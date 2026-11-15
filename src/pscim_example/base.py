from typing import Any

from pydantic import AliasGenerator, BaseModel, ConfigDict, model_validator


def snake_to_camel(string: str) -> str:
    if not string:
        return string
    words = string.split("_")
    return words[0].lower() + "".join(word.capitalize() for word in words[1:])


class SCIMBaseModel(BaseModel):
    """Base model for SCIM data"""

    model_config = ConfigDict(
        extra="forbid",
        alias_generator=AliasGenerator(
            validation_alias=lambda s: s.replace("_", "").lower(),
            serialization_alias=snake_to_camel,
        ),
        use_attribute_docstrings=True,
    )

    @model_validator(mode="before")
    @classmethod
    def normalise_incoming_fields(cls, data: Any) -> Any:
        if isinstance(data, dict):
            return {key.lower(): value for key, value in data.items()}
        return data

    # TODO: Implement the following functions
    # The key must be the validation alias (case-insensitive)
    def __getitem__(self, key: str) -> Any:
        return key.lower()

    def __setitem__(self, key: str, value: Any) -> None:
        self.__getitem__(key)

    def __delitem__(self, key: str) -> None:
        self.__delattr__(key)
