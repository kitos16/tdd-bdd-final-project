import os
import logging
from unittest import TestCase
from service.common import error_handlers, status

class TestErrorHandlers(TestCase):
    """Error Hanlders Tests"""

    def setUp(self):
        """Runs before each test"""
    
    def test_method_not_supported(self):
        """Should get a method not supported error"""
        response = error_handlers.method_not_supported("test error")[0]
        response = response.get_json()
        self.assertEqual(response.get("status"), status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.get("error"), "Method not Allowed")
        self.assertEqual(response.get("message"), "test error")

    def test_internal_server_error(self):
        """Should get a internal server error"""
        response = error_handlers.internal_server_error("test error")[0]
        response = response.get_json()
        self.assertEqual(response.get("status"), status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.get("error"), "Internal Server Error")
        self.assertEqual(response.get("message"), "test error")