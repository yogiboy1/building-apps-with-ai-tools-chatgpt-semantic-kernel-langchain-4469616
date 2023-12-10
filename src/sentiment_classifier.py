import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

while True:
    user_text= input("enter your mood:")
    if(user_text=="exit" or user_text=="quit"):
        break
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a sentient bot you take the user's input about their mood and print out a quote relating to that mood"},
            {"role": "user", "content": user_text}
        ],
        temperature=0.7,
        max_tokens=150,
    )

    response_message = response["choices"][0]["message"]
    print(response_message)
