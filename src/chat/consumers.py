from channels.consumer import SyncConsumer


class ChatConsumer(SyncConsumer):
    def websocket_connect(self, event):
        # when the socket connects
        print(event)

    def websocket_receive(self, event):
        # when the socket connects
        print(event)

    def websocket_disconnect(self, event):
        # when the socket connects
        print(event)