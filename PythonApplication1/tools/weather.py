from tools.base_tool import BaseTool

class WeatherTool(BaseTool):

    def execute(self, city: str):
        return f"The weather in {city} is sunny (demo data)"

    def get_declaration(self):
        return {
            "name": "weather",
            "description": "Get weather information",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string"}
                },
                "required": ["city"]
            }
        }
