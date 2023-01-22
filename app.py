import json
import http.client
import os
from flask import Flask, request
from fortune_teller import FortuneTeller

app = Flask(__name__)
fortune_teller = FortuneTeller()


@app.route('/', methods=['GET'])
def hello_world():
    return '<h1>🐡</h1>'


@app.route('/', methods=['POST'])
def post():
    request_data = type(request.get_data())
    print(request_data)
    request_payload = json.loads(request_data)

    if request_payload['type'] == 'url_verification':
        # slackのchallenge認証を通すために、challengeに入っている文字列をオウム返しする
        return request_data['challenge']
    elif is_target(request_payload):
        channel = request_payload['event']['channel']
        send_message(fortune_teller.tell(), channel)
        return '', 204
    else:
        return 'bad request', 400


def is_target(request_payload):
    return request_payload['type'] == 'event_callback' and \
        request_payload['event']['type'] == 'app_mention'


def send_message(message_str, channel):
    SLACK_POST_MESSAGE_API_URL = "https://slack.com/api/chat.postMessage"
    SLACK_OAUTH_TOKEN = os.environ.get('OAUTH_TOKEN')
    msg_dict = {
        'text': message_str,
        'channel': channel
    }
    conn = http.client.HTTPSConnection("slack.com")
    payload = json.dumps(msg_dict)
    headers = {
        'Content-type': 'application/json',
        "Authorization": "Bearer " + SLACK_OAUTH_TOKEN
    }
    print(f"send_message: {payload}")
    conn.request(
        "POST", SLACK_POST_MESSAGE_API_URL, payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


if __name__ == '__main__':
    app.run()
