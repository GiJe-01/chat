function sendMessage() {
    const input = document.getElementById('messageInput');
    const message = input.value;
    if (message.trim() === '') return;

    const messagesContainer = document.getElementById('messages');
    const userMessage = document.createElement('div');
    userMessage.className = 'message user';
    userMessage.textContent = message;
    messagesContainer.appendChild(userMessage);

    // Simulate bot response
    setTimeout(() => {
        const botMessage = document.createElement('div');
        botMessage.className = 'message bot';
        botMessage.textContent = 'これはボットの返信です。';
        messagesContainer.appendChild(botMessage);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }, 1000);

    input.value = '';
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}
