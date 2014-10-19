$.ajaxSetup ({
	cache: false
});

function populateChat() {
	var url = "/chat";
	$("#ChatHistory").load(url).fail(function(){
		$("#ChatHistory").text("Failed to Load.");});
}

setInterval(populateChat, 1000);
