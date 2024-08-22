const container = document.getElementById('container');
const registerBtn = document.querySelector('.toggle-right .btn');
const loginBtn = document.querySelector('.toggle-left .btn');

if (registerBtn) {
    registerBtn.addEventListener('click', () => {
        container.classList.add("active");
    });
}

if (loginBtn) {
    loginBtn.addEventListener('click', () => {
        container.classList.remove("active");
    });
}