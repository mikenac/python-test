""" This module does boss handling of JSON """

import json
import requests

class JsonMessageHandler(object):
    """ handles json messages like a boss """

    def __init__(self):
        """init"""

    @staticmethod
    def create_template_employee(employee_id):
        """ Add the employee ID to a templated employee """

        local_id = employee_id
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
        # branch for illustration purposes
        if local_id == "35":
            local_id = "75"
        json_tmpl = json.loads(template)
        json_tmpl["job"]["employeeId"] = local_id
        return json.dumps(json_tmpl)

    @staticmethod
    def multiply(num_1, num_2):
        """ Multiply two numbers together """
        return num_1 * num_2

    # example of how to disable warning
    #pylint: disable=missing-docstring
    @staticmethod
    def some_not_covered_function(arg1, arg2):
        return arg1 / arg2

    @staticmethod
    def request_json(url):
        """Get a json object from a REST API"""
        resp = requests.get(url)
        if resp.status_code != 200:
            raise requests.HTTPError(resp.response)
        return resp
