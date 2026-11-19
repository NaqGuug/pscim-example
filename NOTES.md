# Notes while developing library
- Raw Pydantic validation (full user json) takes around 50 microseconds (median)
    - No custom validation, just Pydantic
- URI regex validation is slow
    - Full URI regex adds around 25 microseconds of overhead when validating full user
    - That's 50 % increase
- RFC 7643 does not define primary field for User addresses.
    - See errata [6005](https://errata.rfc-editor.org/eid6005/)
