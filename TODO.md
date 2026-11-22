# TODO

## Schemas attribute
- Resources build schemas list during model validation or init
- Editing schemas is not necessary

## Context (GET, POST differences on characteristics)
- Model validator or field validator by type?
    - Test performance

Request
- Validation: ignore read_only, error if missing required
- Serialisation: ignore read_only

Response
- Validation: never/always errors if present/missing
- Serialisation: Returned characteristics
    - "Always" always retured
    - "Never" never retured
    - "Default" returned except excluded
    - "Request" not returned except included

## Extensions
- How to add/remove extensions as inheritance doesn't work?

## Filter
- Parser a separate module
- Pyparsing

## Patch
- Custom message
- Method to apply patch operations

## Full tests
- Validation
- Dump
- CRUD
- Patch
- Filters

## Documentation
- README

## Canonical values???
- Canonical values are only suggestions, so enums alone can't work
- It's service provider's choice to restrict it or not 

## Custom __getitem__, alias
- __setitem__, delitem???
- Plus extensions, base schema -> create_model
- Is this necessary?
