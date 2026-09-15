from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPEN_API_KEY")

client = OpenAI(api_key=api_key)

response1 = client.chat.completions.create(
    model="gpt-3.5-turbo",
    temperature=0.9,
    messages=[
         {"role": "system", "content": "너는 회사에 관리팀장 역할이야. 그 이야기의 캐릭터에 맞게 분위기와 태도를 유지해줘."},
        #{"role": "system", "content": "너는 영화 배트맨에 나오는 조커 역할이야. 조커는 악당이야. 그 캐릭터에 맞게 답변해줘."},
        {"role": "user", "content": "대체 뭐가 문제인데 일을 똑바로 못 하지?"}
    ]
)

print(response1.choices[0].message.content)