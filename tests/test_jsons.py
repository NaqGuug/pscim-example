from pathlib import Path
from pscim_example import User


fixture_path = Path(__file__).parent / "fixtures"
full_user = (fixture_path / "full_user.json").read_text()


def test_full_user_validation_and_dump():
    """Test full user from RFC 7643 section 8.2 gets validated and dumped."""
    full_user_object = User.model_validate_json(full_user)
    full_user_object.model_dump_json()


# TODO: Test URI validation performance

# uris = [
#     "http://helloworld.com/",
#     "foo+://example.com:8042/over/there?name=ferret#nose",
#     "foo+://andrewj:myPassword:mySecondPassword@example.com:8042/over/there?name=ferret#nose",
#     "http://10.15.20.73/",
#     "http://user.@com/",
#     "urn:example:animal:ferret:nose",
#     "Users/2819c223-7f76-453a-919d-413861904646"
# ]
#
# for uri in uris:
#     match = re_python_rfc3986_URI_reference.match(uri)
#     assert match is not None
#     assert match.string == uri
#     assert match.endpos == len(uri)
