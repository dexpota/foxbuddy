from flask import Flask, Response, stream_with_context
from faker import Faker
from random import randint
from time import sleep
import json


def fake_ai():
    """
    :rtype:
    :return:
    """
    with open("resources/ai.json") as file:
        return json.dumps(json.load(file))


def ai_stream():
    while True:
        sleep(randint(1, 2))
        yield fake_ai() + "\n"


def main():
    fake = Faker()
    app = Flask(__name__)

    @app.route('/ai/stream')
    def stream():
        return Response(ai_stream(),
                        mimetype="text/event-stream")

    @app.route('/searchTweets')
    def search_tweets():
        def generate():
            while True:
                sleep(randint(1, 1))
                yield json.dumps([{'tweet': fake.text()}]).encode('utf-8')

        return Response(stream_with_context(generate()), mimetype='application/json')

    app.run(port=1234)
