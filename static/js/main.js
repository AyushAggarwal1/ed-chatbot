
async function sendMessage() {
    const userInput = document.getElementById('userInput').value;
    if (!userInput) return;

    document.getElementById('messages').innerHTML += `<div class="message user">You: ${userInput}</div>`;
    document.getElementById('userInput').value = '';

    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: userInput }),
        });

        // Check if the response is not okay
        if (!response.ok) {
            const errorData = await response.json();
            document.getElementById('messages').innerHTML += `<div class="message error">Error: ${errorData.detail || 'An error occurred'}</div>`;
            return;
        }

        const data = await response.json();
        document.getElementById('messages').innerHTML += `<div class="message bot">Bot: ${data.response}</div>`;
    } catch (error) {
        document.getElementById('messages').innerHTML += `<div class="message error">Error: ${error.message}</div>`;
    }

    // Scroll to the bottom of the messages
    document.getElementById('messages').scrollTop = document.getElementById('messages').scrollHeight;
}