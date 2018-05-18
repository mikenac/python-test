""" This guys tests like nobody """

import unittest
import json
from unittest.mock import MagicMock
from unittest.mock import patch
import requests
from json_message_processor.json_message_handler import JsonMessageHandler


class TestJsonMessageHandler(unittest.TestCase):
    """tests Json message handling like a boss"""

    def setUp(self):
        """Setup for the test class"""

    def tearDown(self):
        """Teardown for the test class"""

    def test_replace_id(self):
        """ Basic test for replacing the employee id """
        json_text = JsonMessageHandler.create_template_employee("45")
        json_dict = json.loads(json_text)
        self.assertEqual("45", json_dict["job"]["employeeId"])

    def test_replace_id_35(self):
        """ Special case test for the transformation of 35 """
        json_text = JsonMessageHandler.create_template_employee("35")
        json_dict = json.loads(json_text)
        self.assertEqual("75", json_dict["job"]["employeeId"])


    def test_multiplication(self):
        """ Simple multiplication test """
        product = JsonMessageHandler.multiply(2, 2)
        self.assertEqual(4, product)
    
    @patch("requests.get")
    def test_request_succcess(self, mocked_get):
        mocked_get.return_value = MagicMock(status_code=200, response="""{"somethings":"somevalue"}""")
        resp = JsonMessageHandler.request_json("http://www.google.com")
        
        self.assertEqual(200, resp.status_code)

    @patch("requests.get")
    def test_request_failure(self, mocked_get):
        mocked_get.return_value = MagicMock(status_code=500, response="Bad things have happened")
        
        with self.assertRaises(requests.HTTPError):
           JsonMessageHandler.request_json("http://www.google.com")


if __name__ == '__main__':
    unittest.main()
