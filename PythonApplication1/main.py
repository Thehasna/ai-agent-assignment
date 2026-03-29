from agent.agent import Agent
from agent.memory import MemoryManager
from agent.tool_registry import ToolRegistry

from tools.calculator import CalculatorTool
from tools.weather import WeatherTool
from tools.translator import TranslatorTool
from tools.time_tool import TimeTool

def main():

    registry = ToolRegistry()
    memory = MemoryManager()

    registry.register("calculator", CalculatorTool())
    registry.register("weather", WeatherTool())
    registry.register("translator", TranslatorTool())
    registry.register("time", TimeTool())

    agent = Agent(registry, memory)

    print("AI Agent Started (type 'exit' to quit)")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        response = agent.run(user_input)

        print("AI:", response)


if __name__ == "__main__":
    main()
