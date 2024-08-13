"""Tests for the 200 status code."""

# pylint: disable=unnecessary-lambda-assignment
from pytest import mark
from tests.utils import HTTPBasicAuth, HTTPBearerAuth

# Authentication objects for the tests
admin_basic = HTTPBasicAuth(username="admin", password="password")
admin_bearer = HTTPBearerAuth(token="admin-mock-token")


class CommonTestsBase:

    def test_status_code(self, response):
        assert response.status_code == 200


@mark.parametrize("authentication", [admin_basic, admin_bearer], indirect=True)
@mark.parametrize("username", ["user1"], indirect=True)
@mark.parametrize("password", ["pass1"], indirect=True)
class TestInDatabase(CommonTestsBase):

    def test_in_database(self, response):
        raise NotImplementedError
