import openai
import os

openai.api_key = "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"


def chat_with_chatbot(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message,
        temperature=0,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\"\"\""]
    )

    return response.choices[0].text.strip()

while True:
    user_input = input("User: ")

    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break

    chatbot_response = chat_with_chatbot(user_input)
    print("Chatbot:", chatbot_response)

# print(openai.api_key)