function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const errorEl = document.getElementById("error");

    // Clear previous errors
    errorEl.classList.remove('show');

    // Validation
    if (!username || !password) {
        errorEl.textContent = 'Please fill in all fields';
        errorEl.classList.add('show');
        setTimeout(() => errorEl.classList.remove('show'), 3000);
        return;
    }

    fetch("http://localhost:8000/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username: username,
            password: password
        })
    })
    .then(res => res.json())
    .then(data => {
        if (data.access_token) {
            localStorage.setItem("token", data.access_token);
            window.location.href = "predict.html";
        } else {
            // Wrong credentials
            errorEl.textContent = "Login failed - Please enter proper username and password";
            errorEl.classList.add('show');
            setTimeout(() => errorEl.classList.remove('show'), 3000);
        }
    })
    .catch(err => {
        console.error(err);
        errorEl.textContent = "Server error - Please try again later";
        errorEl.classList.add('show');
        setTimeout(() => errorEl.classList.remove('show'), 3000);
    });
}

// Allow Enter key to submit
document.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') login();
});