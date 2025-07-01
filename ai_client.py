import cohere
import os

API_KEY = os.getenv("CO_API_KEY")

co = cohere.ClientV2(api_key=API_KEY)


co = cohere.ClientV2(api_key=API_KEY)


class AIClient:
    def __init__(self):
        self.client = co

    async def generate_text(self, prompt: str) -> str:
        res = self.client.chat(
            model="command-a-03-2025",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )
        return res.message.content[0].text if res.message.content else ""
