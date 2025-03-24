document.getElementById('registerForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const data = {
        username: username,
        email: email,
        password: password
    };

    fetch('/api/user/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
   .then(response => response.json())
   .then(result => {
        const messageDiv = document.getElementById('message');
        if (result.code === 200) {
            messageDiv.textContent = '注册成功！';
        } else {
            messageDiv.textContent = '注册失败：' + result.message;
        }
    })
   .catch(error => {
        const messageDiv = document.getElementById('message');
        messageDiv.textContent = '发生错误：' + error.message;
    });
});