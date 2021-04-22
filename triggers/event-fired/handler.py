from relay_sdk import Interface, WebhookServer
from quart import Quart, request, jsonify, make_response

import logging
import json

relay = Interface()
app = Quart('bitbucket-event')

logging.getLogger().setLevel(logging.INFO)


@app.route('/', methods=['POST'])
async def handler():
    bitbucket_event = request.headers.get('X-Event-Key')

    if bitbucket_event is None:
        return {'message': 'not a valid Bitbucket event'}, 400, {}
    if bitbucket_event == 'ping':
        return {'message': 'success'}, 200, {}

    logging.info("Received event from Bitbucket: {}".format(bitbucket_event))

    event_payload = await request.get_json()
    logging.info("Received the following webhook payload: \n%s", json.dumps(event_payload, indent=4))

    if event_payload is None:
        return {'message': 'not a valid Bitbucket event'}, 400, {}

    relay.events.emit({
          'event_payload': event_payload,
          'bitbucket_event': bitbucket_event
      })

    return {'message': 'success'}, 200, {}


if __name__ == '__main__':
    WebhookServer(app).serve_forever()
