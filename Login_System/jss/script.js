document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    form.addEventListener('submit', (event) => {
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        const messageBox = document.createElement('div');
        messageBox.style.marginTop = '20px';
        form.appendChild(messageBox);
 
        if (username !== '' && password !== '') {
            messageBox.textContent = 'Login successful!';
            messageBox.style.color = 'green';
        } else {
            event.preventDefault();
            messageBox.textContent = 'Both fields are required!';
            messageBox.style.color = 'red';
        }
    });
 
    const button = document.querySelector('button');
    button.addEventListener('mouseover', () => {
        button.style.backgroundColor = '#45a049';
    });
    button.addEventListener('mouseout', () => {
        button.style.backgroundColor = '#4CAF50';
    });
 
    const passwordField = document.getElementById('password');
    const togglePassword = document.createElement('span');
    togglePassword.textContent = 'Show';
    togglePassword.style.cursor = 'pointer';
    togglePassword.style.marginLeft = '10px';
    passwordField.parentNode.appendChild(togglePassword);
 
    togglePassword.addEventListener('click', () => {
        if (passwordField.type === 'password') {
            passwordField.type = 'text';
            togglePassword.textContent = 'Hide';
        } else {
            passwordField.type = 'password';
            togglePassword.textContent = 'Show';
        }
    });
 });
 