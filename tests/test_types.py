import pytest
from pytest_benchmark.fixture import BenchmarkFixture

from pscim_example.types import re_python_rfc3986_URI_reference


@pytest.mark.parametrize("uri", [
    "http://helloworld.com/",
    "foo+://example.com:8042/over/there?name=ferret#nose",
    "foo+://andrewj:myPassword:mySecondPassword@example.com:8042/over/there?name=ferret#nose",
    "http://10.15.20.73/",
    "http://user.@com/",
    "urn:example:animal:ferret:nose",
    "Users/2819c223-7f76-453a-919d-413861904646",
])
def test_uri_validation(benchmark: BenchmarkFixture, uri: str) -> None:
    match = benchmark(re_python_rfc3986_URI_reference.match, uri)
    assert match is not None
    assert match.string == uri
    assert match.endpos == len(uri)
