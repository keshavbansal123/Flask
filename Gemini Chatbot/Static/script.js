async function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value.trim();
    if (!message) return;

    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `
        <div class="message-container user-message">
            <div class="message-sender">You:</div>
            <div class="message-content">${message}</div>
        </div>
    `;
    input.value = "";
    input.style.height = 'auto';

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: message })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        const html = marked.parse(data.reply);

        chatBox.innerHTML += `
            <div class="message-container ai-message">
                <div class="message-sender">AI:</div>
                <div class="message-content">${html}</div>
            </div>
        `;
        chatBox.scrollTop = chatBox.scrollHeight;

    } catch (error) {
        console.error("Error sending message:", error);
        chatBox.innerHTML += `<p class="error-message">Error: Could not retrieve response.</p>`;
    }
}

//  Ensure the DOM is fully loaded before accessing elements
document.addEventListener('DOMContentLoaded', function () {
    const input = document.getElementById('user-input');
    if (input) {
        input.addEventListener('input', function () {
            this.style.height = 'auto';
            this.style.height = (this.scrollHeight) + 'px';
        });
    } else {
        console.error("Error: #user-input element not found!");
    }
});