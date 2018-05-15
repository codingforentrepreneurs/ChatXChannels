import json

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def broadcast_msg_to_chat(msg, group_name, user='admin', event_type='chat_message'):
    channel_layer = get_channel_layer()
    actual_message = json.dumps({'msg': msg, 'user': user})
    broadcast_data = {
        'type': event_type,
        'message': actual_message
    }
    async_to_sync(channel_layer.group_send)(group_name, broadcast_data)