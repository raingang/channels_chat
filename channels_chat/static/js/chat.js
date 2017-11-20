var server = 'ws://' + window.location.host


function startChat(){
	console.log('Connecting')
	ws = new WebSocket(server);
	ws.onopen = function(e){
		console.log('Connected');
	}
	ws.onmessage = function(e){
		var parsed_data = JSON.parse(e.data);
		if(parsed_data['type'] == 'message' | parsed_data['type'] == 'system'){
			var text = parsed_data['text'];
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
            if(parsed_data['type'] == 'system'){
            	user_block.style.color = 'green';
            }
			console.log(parsed_data['text']);
		}
	}
}

function sendMessage(type, text){
	if (text !== ''){
		type = '"' + "type" + '"' + ':' + '"' + type + '"';
		text = '"' + "text" + '"' + ':' + '"' + text + '"';
		var data = '{' + type + ',' + text + '}';
		ws.send(data);
	}
}