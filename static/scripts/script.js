// WebSocket server URL

const serverUrl = "ws://0.0.0.0:6603";

// Create WebSocket connection
const socket = new WebSocket(serverUrl);

// Log errors
socket.onerror = (error) => {
  console.error("WebSocket error: ", error);
};

// Log messages from the server
socket.onmessage = (event) => {
  const messagesDiv = document.getElementById("messages");
  messagesDiv.innerHTML += "<p>" + event.data + "</p>";
};

// Send message to server
function sendMessage() {
  const messageInput = document.getElementById("messageInput");
  const message = messageInput.value;
  socket.send(message);
  messageInput.value = "";
}
