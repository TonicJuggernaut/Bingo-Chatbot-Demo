```python
from flask import Flask, request, jsonify
import os
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/', methods=['POST'])
def handle_message():
    message = request.json['message']

    try:
        response = openai.Completion.create(
            engine='davinci-codex',
            prompt=message,
            max_tokens=100,
            temperature=0.7,
            n=1,
            stop=None
        )

        if response['choices'][0]['finish_reason'] == 'stop':
            return jsonify(message=response['choices'][0]['text'])
        else:
            return jsonify(message='Oops! Something went wrong with the completion.')

    except Exception as e:
        return jsonify(message='Oops! Something went wrong with the API request.')

if __name__ == '__main__':
    app.run()
```
