import os
import openai
from dotenv import load_dotenv
load_dotenv()


def generate_review(review):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a sentiment classification bot working in the healthcare field, print out if the user is happy or sad based on their review on care received . Print only the word happy if they provide a positive feedback.If they are not then identify the gap in care and print out sad along with the name of the gap."},
            {"role": "user", "content": review}
        ],
        temperature=0.7,
        max_tokens=150,
    )

    response_message = response["choices"][0]["message"]["content"]
    if response_message == "happy":
        # TODO 1
        return "thank you for staying with us"
    # TODO 2
    return response_message