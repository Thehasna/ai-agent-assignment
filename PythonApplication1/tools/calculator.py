from tools.base_tool import BaseTool

class CalculatorTool(BaseTool):

    def execute(self, expression: str):
        try:
            return str(eval(expression))
        except:
            return "Invalid math expression"

    def get_declaration(self):
        return {
            "name": "calculator",
            "description": "Perform math calculations",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string"}
                },
                "required": ["expression"]
            }
        }
