import json
from channels.consumer import SyncConsumer


class ChatConsumer(SyncConsumer):
    def websocket_connect(self, event):
        # when the socket connects
        print(event)
        self.send({
            "type": "websocket.accept"
        })


    def websocket_receive(self, event): # websocket.receive
        # when the socket connects
        print(event['text'])
        new_message_data = json.loads(event['text'])
        print(new_message_data)
        self.send({
            "type": "websocket.send",
            "text": json.dumps(new_message_data)
        })

    def websocket_disconnect(self, event):
        # when the socket connects
        print(event)