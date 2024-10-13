from flask import Flask, request
import requests
import json
import re
from openai import OpenAI

app = Flask(__name__)

@app.route('/translate', methods=['get'])
def translate():
    content = request.args.get('text')

    # Check if 'text' parameter is missing
    if content is None:
        return "Missing text content in request!"

    api_key = "输入API KEY"

    Language = "zh"

    # Initialize OpenAI client
    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

    try:
        # Make the request to DeepSeek API
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a professional, authentic translation engine, only returns Simplified Chinese translations. Most context are about video games, especially horror games."},
                {"role": "user", "content": f"Translate the content to {Language} Language:\n\n<Start>{content}<End>"},
            ],
            stream=False
        )

        # Extract translated text
        trans = response.choices[0].message.content

        # Remove unnecessary tags
        trans = re.sub(r"<开始>|<结束>", "", trans)

        # Return translated text
        return trans

    except Exception as e:
        # Handle potential errors during translation
        return f"An error occurred during translation: {e}"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
