from openai import OpenAI


client = OpenAI()

# 모델 - GPT 3.5 Turbo 선택
model = "gpt-4o"

# 메시지 설정하기
messages = [{
    "role": "user",
    "content": """"""
}]

completion = client.chat.completions.create(
    model = model,
    messages = messages
)

print(completion.choices[0].message.content)