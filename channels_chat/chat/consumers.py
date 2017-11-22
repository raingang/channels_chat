import json
from channels import Group
from . import messages
from channels.sessions import http_session, channel_session

@channel_session
@http_session
def ws_connect(message):
	message.reply_channel.send({'accept': True})
	Group('global').add(message.reply_channel)
	message.channel_session['username'] = message.http_session.get('username')
	data = messages.system(text = 'Connection established.')
	message.reply_channel.send(data)

@channel_session
def ws_message(message):
	response = json.loads(message['text'])
	text = response['text']
	data = messages.message(username = message.channel_session['username'], text = text)
	Group('global').send(data)

@http_session
def ws_disconnect(message):
	Group('global').discard(message.reply_channel)
