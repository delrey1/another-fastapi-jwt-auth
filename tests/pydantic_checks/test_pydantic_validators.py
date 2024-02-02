import unittest

import pytest

from another_fastapi_jwt_auth.config import validate_denylist_token_checks, validate_token_location, \
    validate_csrf_methods


def test_validate_denylist_token_checkshappy():
    # Confirm presence of str is fine
    v = "access"
    assert validate_denylist_token_checks(v) == [v]

    # Confirm presence of list is fine
    v = ["access"]
    assert validate_denylist_token_checks(v) == v

    # Confirm presence of list is fine
    v = ["access", "refresh"]
    assert validate_denylist_token_checks(v) == v

    # Confirm presence of list is fine
    v = ["refresh", "access"]
    assert validate_denylist_token_checks(v) == v


def test_validate_denylist_token_checks_unhappy():
    # Confirm presence of str is fine
    v = "accessd"
    with pytest.raises(ValueError, match=r"authjwt_denylist_token_checks"):
        validate_denylist_token_checks(v)

    # Confirm presence of list is fine
    v = ["accessd", "access"]
    with pytest.raises(ValueError, match=r"authjwt_denylist_token_checks"):
        validate_denylist_token_checks(v)


def test_validate_token_location_happy():
    # Confirm presence of str is fine
    v = "headers"
    assert validate_token_location(v) == {v}

    # Confirm presence of list is fine
    v = {"headers"}
    assert validate_token_location(v) == v

    # Confirm presence of list is fine
    v = {"headers", "cookies"}
    assert validate_token_location(v) == v

    # Confirm presence of list is fine
    v = {"headers", "cookies"}
    assert validate_token_location(v) == v


def test_validate_token_location_unhappy():
    # Confirm presence of str is fine
    v = "accessd"
    with pytest.raises(ValueError, match=r"authjwt_token_location"):
        validate_token_location(v)

    # Confirm presence of list is fine
    v = {"accessd", "headers"}
    with pytest.raises(ValueError, match=r"authjwt_token_location"):
        validate_token_location(v)


@pytest.mark.parametrize('i, o', [
    ('get', {'GET'}),
    ('GET', {'GET'}),
    ({'GET'}, {'GET'}),
])
def test_validate_csrf_methods(i, o):
    assert validate_csrf_methods(i) == o


@pytest.mark.parametrize('i', [
    ('gett'),
    ('GEtT'),
    ({'GET', 'GETT'}),
])
def test_validate_csrf_methods(i):
    with pytest.raises(ValueError, match=r"authjwt_csrf_methods"):
        validate_csrf_methods(i)


if __name__ == '__main__':
    unittest.main()
