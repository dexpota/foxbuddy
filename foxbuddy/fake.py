from flask import Flask, Response, stream_with_context
from faker import Faker
from random import randint
from time import sleep
import json


def main():
    fake = Faker()
    app = Flask(__name__)

    @app.route('/searchTweets')
    def search_tweets():
        def generate():
            while True:
                sleep(randint(1, 1))
                yield json.dumps([{'tweet': fake.text()}]).decode('utf-8')

        return Response(stream_with_context(generate()), mimetype='application/json')

    app.run(port=1234)
