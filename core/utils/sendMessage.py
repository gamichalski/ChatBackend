from channels.layers import get_channel_layer

async def send_response_to_user(content):
    channel_layer = get_channel_layer()
    await channel_layer.group_send(
    content['chat'],    
        {
        "type": "chat_message",
        "body": content['body'], #corpo de reuisição
        "user_type": content['user_type'], #Tipo de reuquisição
        }
    )
    
