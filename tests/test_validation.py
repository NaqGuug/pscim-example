import pytest
from pytest_benchmark.fixture import BenchmarkFixture

from pscim_example import ExchangeDirection, User

from .fixtures import FULL_USER, FULL_USER_JSON


@pytest.mark.parametrize("direction", [
    None,
    ExchangeDirection.NONE,
    ExchangeDirection.REQUEST,
    ExchangeDirection.RESPONSE
])
def test_full_user_validation(benchmark: BenchmarkFixture, direction: ExchangeDirection) -> None:
    """Test full user from RFC 7643 section 8.2 gets validated (python)."""
    full_user_object: User = benchmark(User.model_validate, FULL_USER, scim_direction=direction)

    # Check normal attributes
    assert full_user_object.user_name == "bjensen@example.com"
    assert full_user_object.name is not None
    assert full_user_object.name.given_name == "Barbara"
    assert full_user_object.emails is not None
    assert {email.value for email in full_user_object.emails} == {"bjensen@example.com", "babs@jensen.org"}

    # Check attributes based on characteristics
    if direction == ExchangeDirection.REQUEST:
        assert full_user_object.id is None
    else:
        assert full_user_object.id == "2819c223-7f76-453a-919d-413861904646"


@pytest.mark.parametrize("direction", [
    None,
    ExchangeDirection.NONE,
    ExchangeDirection.REQUEST,
    ExchangeDirection.RESPONSE
])
def test_full_user_validation_json(benchmark: BenchmarkFixture, direction: ExchangeDirection) -> None:
    """Test full user from RFC 7643 section 8.2 gets validated (json)."""
    full_user_object: User = benchmark(User.model_validate_json, FULL_USER_JSON, scim_direction=direction)

    # Check normal attributes
    assert full_user_object.user_name == "bjensen@example.com"
    assert full_user_object.name is not None
    assert full_user_object.name.given_name == "Barbara"
    assert full_user_object.emails is not None
    assert {email.value for email in full_user_object.emails} == {"bjensen@example.com", "babs@jensen.org"}

    # Check attributes based on characteristics
    if direction == ExchangeDirection.REQUEST:
        assert full_user_object.id is None
    else:
        assert full_user_object.id == "2819c223-7f76-453a-919d-413861904646"
