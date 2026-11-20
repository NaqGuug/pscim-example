from datetime import datetime
from typing import Annotated

from ..base import SCIMBaseModel
from ..characteristics import (
    CaseExact,
    Mutability,
    Returned,
    Uniqueness,
)
from ..types import URI, ComplexAttribute


class Meta(ComplexAttribute):
    resource_type: Annotated[
        str | None,
        CaseExact.TRUE,
        Mutability.READ_ONLY
    ] = None
    """The name of the resource type of the resource."""

    created: Annotated[datetime | None, Mutability.READ_ONLY] = None
    """The "DateTime" that the resource was added to the service provider."""

    last_modified: Annotated[datetime | None, Mutability.READ_ONLY] = None
    """The most recent DateTime that the details of this resource were updated at the service provider."""

    location: Annotated[URI | None, Mutability.READ_ONLY] = None
    """The URI of the resource being returned."""

    version: Annotated[
        str | None,
        CaseExact.TRUE,
        Mutability.READ_ONLY
    ] = None
    """The version of the resource being returned."""


class Resource(SCIMBaseModel):
    """Base model for resources"""

    # TODO: Remove
    schemas: list[URI] | None = None
    """List of schemas"""

    id: Annotated[
        str | None,
        CaseExact.TRUE,
        Mutability.READ_ONLY,
        Returned.ALWAYS,
        Uniqueness.GLOBAL  # Or server
    ] = None
    """A unique identifier for a SCIM resource as defined by the service provider."""

    external_id: Annotated[str | None, CaseExact.TRUE] = None
    """A String that is an identifier for the resource as defined by the provisioning client."""

    meta: Annotated[Meta | None, Mutability.READ_ONLY] = None
    """A complex attribute containing resource metadata."""
