from enum import Enum, StrEnum, auto


class Required(Enum):
    TRUE = True
    FALSE = False


# TODO: Canonical values here or Pydantic examples block?


class CaseExact(Enum):
    TRUE = True
    FALSE = False


class Mutability(StrEnum):
    READ_ONLY = "readOnly"
    READ_WRITE = "readWrite"
    IMMUTABLE = "immutable"
    WRITE_ONLY = "writeOnly"


class Returned(StrEnum):
    ALWAYS = "always"
    NEVER = "never"
    DEFAULT = "default"
    REQUEST = "request"


class Uniqueness(StrEnum):
    NONE = "none"
    SERVER = "server"
    GLOBAL = "global"


class ExchangeDirection(Enum):
    NONE = auto()
    REQUEST = auto()
    RESPONSE = auto()
