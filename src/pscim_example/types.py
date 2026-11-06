from pydantic import Field
from .base import SCIMBaseModel


class URI(str):
    """Uniform Resource Identifier"""


class ComplexAttribute(SCIMBaseModel):
    """Complex attribute type"""


class MultiValuedComplexAttribute(ComplexAttribute):
    """Multi-valued complex attribute type"""

    type: str | None = None
    """A label indicating the attribute's function, e.g., "work" or "home"."""

    primary: bool | None = None
    """A Boolean value indicating the 'primary' or preferred attribute value for this attribute."""

    display: str | None = None
    """A human-readable name, primarily used for display purposes."""

    value: str | None = None
    """The attribute's significant value, e.g., email address, phone number."""

    ref: URI | None = Field(None, alias="$ref")
    """The reference URI of a target resource, if the attribute is a reference."""
