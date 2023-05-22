from flask import Flask, request
import openai
from openai import InvalidRequestError
from openai.error import APIConnectionError

app = Flask(__name__)
app.secret_key = "secret_key"
openai.api_key = "openai_key"


@app.route("/aigc/chat", methods=["post"])
def chat():
    data = request.json
    prompt = data.get("prompt")
    messages = [{"role": "user", "content": prompt}]
    try:
        completions = openai.ChatCompletion.create(
            messages=messages,
            model="gpt-3.5-turbo"
        )
        return completions.choices[0]["message"]["content"]
    except InvalidRequestError:
        return "InvalidRequestError"
    except APIConnectionError or TimeoutError:
        return "APIConnectionError"


@app.route("/aigc/image", methods=["post"])
def image():
    data = request.json
    prompt = data.get("prompt")

    try:
        image_url = openai.Image.create(
            prompt=prompt,
            response_format="url",
            n=1,
            size="1024x1024"
        )["data"][0]["url"]
        return image_url
    except InvalidRequestError:
        return "InvalidRequestError"
    except APIConnectionError or TimeoutError:
        return "APIConnectionError"
