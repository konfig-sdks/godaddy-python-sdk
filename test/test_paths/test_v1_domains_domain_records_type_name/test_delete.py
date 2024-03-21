# coding: utf-8

"""
    All the help and tools you need to grow online: Websites, Domains, Digital and Social Marketing - plus GoDaddy Guides with you every step of the way.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import godaddy_python_sdk
from godaddy_python_sdk.paths.v1_domains_domain_records_type_name import delete
from godaddy_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1DomainsDomainRecordsTypeName(ApiTestMixin, unittest.TestCase):
    """
    V1DomainsDomainRecordsTypeName unit test stubs
        Delete all DNS Records for the specified Domain with the specified Type and Name
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''


if __name__ == '__main__':
    unittest.main()
