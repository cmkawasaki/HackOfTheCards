$.ajaxSetup ({
	cache: false
});

function populateChat() {
	var url = "/chat";
	$("#ChatHistory").load(url);
}

function chatSubmit() {
	$.ajax({ type: "POST", url: '/write', data:$('#ChatForm').serializeArray()});
	populateChat();
	return false;
}
	
setInterval(populateChat, 1000);
