class ToolRegistry:
    def __init__(self):
        self.tools = {}

    def register(self, name, tool):
        self.tools[name] = tool

    def get_tool(self, name):
        return self.tools.get(name)

    def execute(self, name, args):
        tool = self.get_tool(name)

        if not tool:
            return f"Error: Tool '{name}' not found"

        try:
            return tool.execute(**args)
        except Exception as e:
            return f"Tool error: {str(e)}"

    def get_declarations(self):
        return [tool.get_declaration() for tool in self.tools.values()]
