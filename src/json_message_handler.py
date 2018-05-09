""" This module does boss handling of JSON """

import json

class JsonMessageHandler:
    """ handles json messages like a boss """

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
        if local_id == "35":
            local_id = "75"
        json_tmpl = json.loads(template)
        json_tmpl["job"]["employeeId"] = local_id
        return json.dumps(json_tmpl)

    @staticmethod
    def multiply(num_1, num_2):
        """ Multiply two numbers together """
        return num_1 * num_2
