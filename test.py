from openai import OpenAI
import os

#os.environ['NVIDIA_API_KEY']=os.getenv("NVIDIA_API_KEY")
KEY = os.getenv("NVIDIA_API_KEY")

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = KEY
)

completion = client.chat.completions.create(
  model="meta/llama3-70b-instruct",
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

