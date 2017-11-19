var server = 'ws://' + window.location.host


function startChat(){
	console.log('Connecting')
	ws = new WebSocket(server);
	ws.onopen = function(e){
		console.log('Connected');
	}
	ws.onmessage = function(e){
		var parsed_data = JSON.parse(e.data);
		if(parsed_data['action'] == 'post_message'){
			var text = parsed_data['data'];
			var username = parsed_data['username'] + ': ';
			var text_node = document.createTextNode(text);
			var username_node = document.createTextNode(username);
			var chat_block = document.getElementById('chat');
			var message_block = document.createElement('div');
			message_block.className += 'message clearfix';
			chat_block.appendChild(message_block);
			var user_block = document.createElement('div');
			var text_block = document.createElement('div');
			message_block.appendChild(user_block);
			message_block.appendChild(text_block);
			text_block.appendChild(text_node);
			user_block.appendChild(username_node);
			text_block.className += 'message__text';
			user_block.className += 'message__user';

			console.log(parsed_data['data']);
		}
	}
}

function sendMessage(action, data){
	if (data !== ''){
		action = '"' + "action" + '"' + ':' + '"' + action + '"';
		data = '"' + "data" + '"' + ':' + '"' + data + '"';
		var content = '{' + action + ',' + data + '}';
		ws.send(content);
	}
}