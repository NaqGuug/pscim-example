from datetime import datetime
from .resource import Resource
from ..types import URI, ComplexAttribute, MultiValuedComplexAttribute


class Name(ComplexAttribute):
    formatted: str | None = None
    """The full name, including all middle names, titles, and suffixes as appropriate, formatted for display"""

    family_name: str | None = None
    """The family name of the User, or last name in most Western languages"""

    given_name: str | None = None
    """The given name of the User, or first name in most Western languages"""

    middle_name: str | None = None
    """The middle name(s) of the User"""

    honorific_prefix: str | None = None
    """The honorific prefix(es) of the User, or title in most Western languages"""

    honorific_suffix: str | None = None
    """The honorific suffix(es) of the User, or suffix in most Western languages"""


class Email(MultiValuedComplexAttribute):
    """Email"""


class PhoneNumber(MultiValuedComplexAttribute):
    """Phone number"""


class Ims(MultiValuedComplexAttribute):
    """Instant messaging address"""


class Photo(MultiValuedComplexAttribute):
    """Photo"""


class Address(MultiValuedComplexAttribute):
    """Address"""

    formatted: str | None = None
    """The full mailing address, formatted for display or use with a mailing label."""

    street_address: str | None = None
    """The full street address component."""

    locality: str | None = None
    """The city or locality component."""

    region: str | None = None
    """The state or region component."""

    postal_code: str | None = None
    """The zip code or postal code component."""

    country: str | None = None
    """The country name component."""

    type: str | None = None
    """Type"""


class Group(MultiValuedComplexAttribute):
    """Group"""


class Entitlement(MultiValuedComplexAttribute):
    """Entitlement"""


class Role(MultiValuedComplexAttribute):
    """Role"""


class X509Certificate(MultiValuedComplexAttribute):
    """X.509 Certificate"""


class User(Resource):
    """User resource"""

    user_name: str | None = None
    """A service provider's unique identifier for the user"""

    name: Name | None = None
    """The components of the user's name."""

    display_name: str | None = None
    """The name of the user, suitable for display to end-users."""

    nick_name: str | None = None
    """The casual way to address the user in real life."""

    profile_url: URI | None = None
    """A URI that is a uniform resource locator that points to a location representing the user's online profile."""

    title: str | None = None
    """The user's title, such as "Vice President"."""

    user_type: str | None = None
    """Used to identify the relationship between the organization and the user."""

    preferred_language: str | None = None
    """Indicates the user's preferred written or spoken languages."""

    locale: str | None = None
    """Used to indicate the User's default location."""

    timezone: str | None = None
    """The User's time zone, in IANA Time Zone database format."""

    active: bool | None = None
    """A Boolean value indicating the user's administrative status."""

    password: str | None = None
    """This attribute is intended to be used as a means to set, replace, or compare a password."""

    emails: list[Email] | None = None
    """Email addresses for the User."""

    phone_numbers: list[PhoneNumber] | None = None
    """Phone numbers for the user."""

    ims: list[Ims] | None = None
    """Instant messaging address for the user."""

    photos: list[Photo] | None = None
    """A URI that is a uniform resource locator that points to a resource location representing the user's image."""

    addresses: list[Address] | None = None
    """A physical mailing address for this user."""

    groups: list[Group] | None = None
    """A list of groups to which the user belongs."""

    entitlements: list[Entitlement] | None = None
    """A list of entitlements for the user that represent a thing the user has."""

    roles: list[Role] | None = None
    """A list of roles for the user that collectively represent who the user is."""

    x509_certificates: list[X509Certificate] | None = None
    """A list of certificates associated with the resource."""
