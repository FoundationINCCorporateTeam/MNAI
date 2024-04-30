function sendMessage() {
    var userInput = document.getElementById("user-input").value;
    appendMessage("You: " + userInput);

    // Send the user input to the server
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/message", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            appendMessage("Bot: " + response.message);
        }
    };
    xhr.send(JSON.stringify({ message: userInput }));
}

function appendMessage(message) {
    var chatBox = document.getElementById("chat-box");
    var p = document.createElement("p");
    p.textContent = message;
    chatBox.appendChild(p);
    chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to bottom
}
