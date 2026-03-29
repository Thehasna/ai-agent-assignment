import google.generativeai as genai
import os

class Agent:

    def __init__(self, registry, memory):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

        self.model = genai.GenerativeModel("gemini-pro")
        self.registry = registry
        self.memory = memory

    def run(self, user_input):
        try:
            self.memory.add("user", user_input)

            response = self.model.generate_content(
                contents=self.memory.get()
            )

            text = response.text

            self.memory.add("assistant", text)

            return text

        except Exception as e:
            return f"Agent error: {str(e)}"
