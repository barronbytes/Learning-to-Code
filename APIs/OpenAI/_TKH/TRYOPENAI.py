import os
from openai import OpenAI


client = OpenAI(api_key=os.getenv("API_OPENAI"))
DEV_CONTEXT = "Take into account the current market outlooks and tailor next actions for a beginner who is just getting started in data science. Response shold only be four sentences at most."


completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
	    { "role": "developer",  "content": DEV_CONTEXT },
        { "role": "user",  "content": input("Ask your data science career question: ") }
    ]
)


print(completion.choices[0].message.content)