"""
# TODO: Update test case description
"""
import pytest
from dsu.test_cases.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX, URL_BASE_PATH


class TestCase01LoginUserAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    URL_BASE_PATH = URL_BASE_PATH
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {}

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {'user_email': 'string@string.com'}
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
