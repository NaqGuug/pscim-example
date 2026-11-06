from datetime import datetime
from ..base import SCIMBaseModel
from ..types import ComplexAttribute, URI


class Meta(ComplexAttribute):
    resource_type: str | None = None
    """The name of the resource type of the resource."""

    created: datetime | None = None
    """The "DateTime" that the resource was added to the service provider."""

    last_modified: datetime | None = None
    """The most recent DateTime that the details of this resource were updated at the service provider."""

    location: URI | None = None
    """The URI of the resource being returned."""

    version: str | None = None
    """The version of the resource being returned."""


class Resource(SCIMBaseModel):
    """Base model for resources"""

    id: str | None = None
    """A unique identifier for a SCIM resource as defined by the service provider."""

    external_id: str | None = None
    """A String that is an identifier for the resource as defined by the provisioning client."""

    meta: Meta | None = None
    """A complex attribute containing resource metadata."""
