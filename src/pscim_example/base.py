from typing import Any
from pydantic.alias_generators import to_camel
from pydantic import BaseModel, ConfigDict, AliasGenerator, model_validator


class SCIMBaseModel(BaseModel):
    """Base model for SCIM data"""

    model_config = ConfigDict(
        extra="forbid",
        alias_generator=AliasGenerator(
            validation_alias=lambda s: s.replace("_", "").lower(),
            # TODO: This capitalises characters after special ones (e.g. $ref -> $Ref) 
            # However, on those cases the serialisation alias should be overriden
            serialization_alias=to_camel
        ),
        use_attribute_docstrings=True,
    )

    @model_validator(mode="before")
    @classmethod
    def normalise_incoming_fields(cls, data: Any) -> Any:
        if isinstance(data, dict):
            return {key.lower(): value for key, value in data.items()}
        return data
