from collections.abc import Callable
from typing import Any, Literal, Self

from pydantic import (
    AliasGenerator,
    BaseModel,
    ConfigDict,
    model_validator,
)
from pydantic.config import ExtraValues
from pydantic.main import IncEx

from .characteristics import ExchangeDirection


def snake_to_camel(string: str) -> str:
    if not string:
        return string
    words = string.split("_")
    return words[0].lower() + "".join(word.capitalize() for word in words[1:])


class SCIMBaseModel(BaseModel):
    """Base model for SCIM data"""

    model_config = ConfigDict(
        extra="forbid",
        validate_by_alias=True,
        serialize_by_alias=True,
        alias_generator=AliasGenerator(
            validation_alias=lambda s: s.replace("_", "").lower(),
            serialization_alias=snake_to_camel,
        ),
        use_attribute_docstrings=True,
        allow_inf_nan=False,
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

    def model_dump(
        self,
        scim_direction: ExchangeDirection | None = ExchangeDirection.NONE,
        *,
        mode: Literal['json', 'python'] | str = 'python',
        include: IncEx | None = None,
        exclude: IncEx | None = None,
        context: dict[str, Any] | None = None,
        by_alias: bool | None = None,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
        exclude_computed_fields: bool = False,
        round_trip: bool = False,
        warnings: bool | Literal['none', 'warn', 'error'] = True,
        fallback: Callable[[Any], Any] | None = None,
        serialize_as_any: bool = False,
        polymorphic_serialization: bool | None = None,
    ) -> dict[str, Any]:
        if scim_direction is not None:
            context = context or {}
            context["scim_direction"] = scim_direction
            mode = "json"
            exclude_none = True
        return super().model_dump(
            mode=mode,
            include=include,
            exclude=exclude,
            context=context,
            by_alias=by_alias,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
            exclude_computed_fields=exclude_computed_fields,
            round_trip=round_trip,
            warnings=warnings,
            fallback=fallback,
            serialize_as_any=serialize_as_any,
            polymorphic_serialization=polymorphic_serialization
        )

    def model_dump_json(
        self,
        scim_direction: ExchangeDirection | None = ExchangeDirection.NONE,
        *,
        indent: int | None = None,
        ensure_ascii: bool = False,
        include: IncEx | None = None,
        exclude: IncEx | None = None,
        context: dict[str, Any] | None = None,
        by_alias: bool | None = None,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
        exclude_computed_fields: bool = False,
        round_trip: bool = False,
        warnings: bool | Literal['none', 'warn', 'error'] = True,
        fallback: Callable[[Any], Any] | None = None,
        serialize_as_any: bool = False,
        polymorphic_serialization: bool | None = None,
    ) -> str:
        if scim_direction is not None:
            context = context or {}
            context["scim_direction"] = scim_direction
            exclude_none = True
        return super().model_dump_json(
            indent=indent,
            ensure_ascii=ensure_ascii,
            include=include,
            exclude=exclude,
            context=context,
            by_alias=by_alias,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
            exclude_computed_fields=exclude_computed_fields,
            round_trip=round_trip,
            warnings=warnings,
            fallback=fallback,
            serialize_as_any=serialize_as_any,
            polymorphic_serialization=polymorphic_serialization
        )

    @classmethod
    def model_validate(
        cls,
        obj: Any,
        scim_direction: ExchangeDirection | None = ExchangeDirection.NONE,
        *,
        strict: bool | None = None,
        extra: ExtraValues | None = None,
        from_attributes: bool | None = None,
        context: dict[str, Any] | None = None,
        by_alias: bool | None = None,
        by_name: bool | None = None,
    ) -> Self:
        if scim_direction is not None:
            context = context or {}
            context["scim_direction"] = scim_direction
        return super().model_validate(
            obj=obj,
            strict=strict,
            extra=extra,
            from_attributes=from_attributes,
            context=context,
            by_alias=by_alias,
            by_name=by_name
        )

    @classmethod
    def model_validate_json(
        cls,
        json_data: str | bytes | bytearray,
        scim_direction: ExchangeDirection | None = ExchangeDirection.NONE,
        *,
        strict: bool | None = None,
        extra: ExtraValues | None = None,
        context: dict[str, Any] | None = None,
        by_alias: bool | None = None,
        by_name: bool | None = None,
    ) -> Self:
        if scim_direction is not None:
            context = context or {}
            context["scim_direction"] = scim_direction
        return super().model_validate_json(
            json_data=json_data,
            strict=strict,
            extra=extra,
            context=context,
            by_alias=by_alias,
            by_name=by_name
        )
