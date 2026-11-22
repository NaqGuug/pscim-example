from pathlib import Path

from pytest_benchmark.fixture import BenchmarkFixture

from pscim_example import User

fixture_path = Path(__file__).parent / "fixtures"
full_user = (fixture_path / "full_user.json").read_text()


# TODO: Parametrize with different contexts (Normal vs. POST)
def test_full_user_validation_json(benchmark: BenchmarkFixture) -> None:
    """Test full user from RFC 7643 section 8.2 gets validated."""
    full_user_object: User = benchmark(User.model_validate_json, full_user)
    assert full_user_object.id == "2819c223-7f76-453a-919d-413861904646"
    assert full_user_object.name is not None
    assert full_user_object.name.given_name == "Barbara"
    assert full_user_object.emails is not None
    assert {email.value for email in full_user_object.emails} == {"bjensen@example.com", "babs@jensen.org"}


# TODO: Parametrize with different contexts (Normal vs. GET)
def test_full_user_dump_json(benchmark: BenchmarkFixture) -> None:
    """Test full user from RFC 7643 section 8.2 gets dumped."""
    # NOTE: This test depends on correct user is validation
    full_user_object: User = User.model_validate_json(full_user)
    dump = benchmark(full_user_object.model_dump_json)
    assert "userName" in dump
    assert "null" not in dump
