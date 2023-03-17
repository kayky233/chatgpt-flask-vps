// 加入回车提交支持，shift+回车换行
var input = document.getElementById("chatinput");
input.addEventListener("keydown", function (event) {
    if (event.keyCode === 13 && !event.shiftKey) {
        event.preventDefault();
        document.getElementById("sendbutton").click();
    }
});
// 设置默认输入
//init_message="你好";
// Send the message to the chatbot
//var xhr = new XMLHttpRequest();
//xhr.open("GET", "/get?msg=" + init_message);
//xhr.send();
//xhr.onload = function () {
	// Append the chatbot's response to the chatlog
	////var chatlog = document.getElementById("chatlog");
	//var response = document.createElement("div");
	//response.innerHTML = "🤔<br>" + init_message + "<br>🤖" + marked.parse(xhr.responseText);
        //chatlog.appendChild(response);
        // Scroll the chatlog to the bottom
        //chatlog.scrollTop = chatlog.scrollHeight;
        //loading.style.display = 'none';
        //}
//document.getElementById("chatinput").value = "";
// Add your JavaScript here
document.getElementById("sendbutton").addEventListener("click", function () {
    let loading = document.getElementById('loading');
    loading.style.display = 'block';
    // Get the user's message from the input field
    var message = document.getElementById("chatinput").value;
    if (message.length < 1) {
        var response = document.createElement("div");
        response.innerHTML = "🤔<br>🤖<br>Message cannot be null\n问题不能为空";
        chatlog.appendChild(response);
        // Scroll the chatlog to the bottom
        chatlog.scrollTop = chatlog.scrollHeight;
        loading.style.display = 'none';
    } else {
        // Clear the input field
        document.getElementById("chatinput").value = "";
        // Send the message to the chatbot
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "/get?msg=" + message);
        xhr.send();
        xhr.onload = function () {
            // Append the chatbot's response to the chatlog
            var chatlog = document.getElementById("chatlog");
            var response = document.createElement("div");
            response.innerHTML = "🤔<br>" + message + "<br>🤖" + marked.parse(xhr.responseText);
            chatlog.appendChild(response);
            // Scroll the chatlog to the bottom
            chatlog.scrollTop = chatlog.scrollHeight;
            loading.style.display = 'none';
        }
    }
});

// 点击按钮时显示弹出框和图片
document.getElementById("showImage").addEventListener("click", function() {
	let image = document.getElementById("myImage");
	image.style.display='none';
});


