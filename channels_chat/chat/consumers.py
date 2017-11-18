import json
from channels import Group 

def ws_connect(message):
	message.reply_channel.send({'accept': True})
	Group('global').add(message.reply_channel)
	content = {'text': json.dumps({"action": "post_message",
		                           "username": 'Server',
		                           "data": 'Connection established.'})}
	message.reply_channel.send(content)

def ws_message(message):
	response = json.loads(message['text'])
	data = response['data']
	content = {'text': json.dumps({'action': 'post_message',
		                           'username': 'Unknown',
		                           'data': data,})}
	Group('global').send(content)

def ws_disconnect(message):
	Group('global').discard(message.reply_channel)