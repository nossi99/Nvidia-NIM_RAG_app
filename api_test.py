from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
nvidia_api_key = os.getenv('NVIDIA_API_KEY')

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = nvidia_api_key
)

completion = client.chat.completions.create(
  model="meta/llama-3.1-8b-instruct",
  messages=[
    {"role": "system", "content": "Du bist ein hilfreicher Assistent, der fließend Deutsch spricht."},
    {"role":"user","content":"Wer ist Olaf Scholz?"}
  ],
  temperature=0.5,
  top_p=1,
  max_tokens=1024,
  stream=True
)

for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")

