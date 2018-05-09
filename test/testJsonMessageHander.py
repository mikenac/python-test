#!/usr/bin/env python3

import unittest
import importlib
import json
from src.JsonMessageHandler import *

class JsonMessageHandlerTests (unittest.TestCase):
	
	def setupUp(self):
		''' Setup for the test class '''

	def tearDown(self):
		''' Teardown for the test class '''

	def test_replace_id(self):
		handler = JsonMessageHandler()
		json_text = handler.createTemplateEmployeeOutput("45")
		json_dict = json.loads(json_text)
		self.assertEqual("45", json_dict["job"]["employeeId"])

	def test_replace_id_35(self):
		handler = JsonMessageHandler()
		json_text = handler.createTemplateEmployeeOutput("35")
		json_dict = json.loads(json_text)
		self.assertEqual("75", json_dict["job"]["employeeId"])	


if __name__ == '__main__':
    unittest.main()