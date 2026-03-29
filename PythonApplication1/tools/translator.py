from tools.base_tool import BaseTool

class TranslatorTool(BaseTool):

    def execute(self, text: str):
        return f"Translated text: {text}"

    def get_declaration(self):
        return {
            "name": "translator",
            "description": "Translate text",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {"type": "string"}
                },
                "required": ["text"]
            }
        }
