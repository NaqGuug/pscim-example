from typing import Any

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
def test_full_user_dump(benchmark: BenchmarkFixture, direction: ExchangeDirection) -> None:
    """Test full user from RFC 7643 section 8.2 gets dumped (python)."""
    # NOTE: This test depends on correct user validation
    full_user_object: User = User.model_validate(FULL_USER)
    dump: dict[str, Any] = benchmark(full_user_object.model_dump, scim_direction=direction)

    # Check normal attributes
    assert "userName" in dump
    assert "username" not in dump
    assert "user_name" not in dump

    # Check attributes based on characteristics
    if direction is not None:
        for value in dump.values():
            assert value is not None
            if isinstance(value, dict):
                assert None not in value.values()

    if direction == ExchangeDirection.REQUEST:
        assert "id" not in dump
    else:
        assert "id" in dump


@pytest.mark.parametrize("direction", [
    None,
    ExchangeDirection.NONE,
    ExchangeDirection.REQUEST,
    ExchangeDirection.RESPONSE
])
def test_full_user_dump_json(benchmark: BenchmarkFixture, direction: ExchangeDirection) -> None:
    """Test full user from RFC 7643 section 8.2 gets dumped (json)."""
    # NOTE: This test depends on correct user validation
    full_user_object: User = User.model_validate_json(FULL_USER_JSON)
    dump: str = benchmark(full_user_object.model_dump_json, scim_direction=direction)

    # Check normal attributes
    assert "userName" in dump
    assert "username" not in dump
    assert "user_name" not in dump

    # Check attributes based on characteristics
    if direction is not None:
        assert "null" not in dump

    if direction == ExchangeDirection.REQUEST:
        assert "lastModified" not in dump
    else:
        assert "lastModified" in dump
