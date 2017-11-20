import json
from channels import Group
from . import messages
from channels.sessions import channel_session

def ws_connect(message):
	message.reply_channel.send({'accept': True})
	Group('global').add(message.reply_channel)
	data = messages.system(text = 'Connection established.')
	message.reply_channel.send(data)

def ws_message(message):
	response = json.loads(message['text'])
	text = response['text']
	data = messages.message(username = 'Unknown', text = text)
	Group('global').send(data)

def ws_disconnect(message):
	Group('global').discard(message.reply_channel)
