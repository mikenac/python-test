""" This guys tests like nobody """

import unittest
import json
from src.json_message_handler import JsonMessageHandler


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


if __name__ == '__main__':
    unittest.main()
