document.addEventListener('DOMContentLoaded', function () {
    const body = document.body;
    const increaseFontBtn = document.getElementById('increase-font');
    const decreaseFontBtn = document.getElementById('decrease-font');
    const toggleContrastBtn = document.getElementById('toggle-contrast');
    
    let fontSize = 16; // Tamaño de fuente inicial en píxeles
    const minFontSize = 12;
    const maxFontSize = 24;

    increaseFontBtn.addEventListener('click', function () {
        if (fontSize < maxFontSize) {
            fontSize++;
            body.style.fontSize = fontSize + 'px';
        }
    });

    decreaseFontBtn.addEventListener('click', function () {
        if (fontSize > minFontSize) {
            fontSize--;
            body.style.fontSize = fontSize + 'px';
        }
    });

    toggleContrastBtn.addEventListener('click', function () {
        body.classList.toggle('high-contrast');
    });
});
