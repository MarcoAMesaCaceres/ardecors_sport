document.addEventListener("DOMContentLoaded", function() {
    // Crear balones flotantes
    for (let i = 0; i < 10; i++) {
        let balloon = document.createElement('div');
        balloon.classList.add('balloon');
        balloon.style.width = balloon.style.height = Math.random() * 100 + 50 + 'px';
        balloon.style.backgroundColor = getRandomColor();
        balloon.style.left = Math.random() * 100 + '%';
        balloon.style.top = Math.random() * 100 + '%';
        document.body.appendChild(balloon);
    }

    // Obtener color aleatorio
    function getRandomColor() {
        let letters = '0123456789ABCDEF';
        let color = '#';
        for (let i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
    }
});