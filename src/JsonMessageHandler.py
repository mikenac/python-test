#!/usr/bin/env python3

import json

class JsonMessageHandler:

	def createTemplateEmployeeOutput (self, id):
		""" Add the employee ID to a templated employee """

		template = """
		{
			"name": "fred",
			"type": "person",
			"job": {
				"company": "intercorp",
				"employeeId": ""
			}
		}
		"""
		if (id == "35"):
			id = "75"
		json_tmpl = json.loads(template)
		json_tmpl["job"]["employeeId"] = id
		return json.dumps(json_tmpl)
