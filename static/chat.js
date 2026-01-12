const form = document.getElementById('chat-form');
const input = document.getElementById('input');
const messagesDiv = document.getElementById('messages');

function appendMessage(role, text) {
  const el = document.createElement('div');
  el.className = 'message ' + role;
  el.innerText = text;
  messagesDiv.appendChild(el);
  messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const text = input.value.trim();
  if (!text) return;
  appendMessage('user', text);
  input.value = '';

  try {
    const resp = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: text, model: DEFAULT_MODEL })
    });
    const data = await resp.json();
    if (resp.ok) {
      appendMessage('assistant', data.reply);
    } else {
      appendMessage('assistant', 'Error: ' + (data.error || JSON.stringify(data)));
    }
  } catch (err) {
    appendMessage('assistant', 'Network error: ' + err.message);
  }
});
