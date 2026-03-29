import datetime
from tools.base_tool import BaseTool

class TimeTool(BaseTool):

    def execute(self):
        return str(datetime.datetime.now())

    def get_declaration(self):
        return {
            "name": "time",
            "description": "Get current time",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
