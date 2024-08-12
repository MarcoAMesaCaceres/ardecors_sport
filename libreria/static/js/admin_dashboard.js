document.addEventListener('DOMContentLoaded', function() {
    console.log("Admin Dashboard Loaded");
});






const toggleInicioButton = document.getElementById('toggle-inicio');
const toggleButtons = document.getElementById('toggle-buttons');
const toggleContrastButton = document.getElementById('toggle-contrast');
const toggleZoomInButton = document.getElementById('toggle-zoom-in');
const toggleZoomOutButton = document.getElementById('toggle-zoom-out');
const rootElement = document.documentElement;

// Mínimo y máximo tamaño de fuente
const MIN_FONT_SIZE = 13;
const MAX_FONT_SIZE = 20;

// Mostrar/ocultar panel de botones de accesibilidad
toggleInicioButton.addEventListener('click', () => {
    toggleButtons.classList.toggle('visible');
});

// Ocultar panel de botones al hacer clic fuera de él
document.addEventListener('click', (event) => {
    if (!toggleButtons.contains(event.target) && !toggleInicioButton.contains(event.target)) {
        toggleButtons.classList.remove('visible');
    }
});

// Alternar contraste y guardar preferencia en el almacenamiento local
toggleContrastButton.addEventListener('click', () => {
  const isContrastEnabled = rootElement.classList.toggle('contrast');
  applyImageContrast();
  localStorage.setItem('contrastSetting', isContrastEnabled);
  console.log('Contraste activado:', isContrastEnabled);

  // Guarda la preferencia del contraste en el almacenamiento local
  localStorage.setItem('contrastSetting', isContrastEnabled);
  new Notification('La función se encuentra en desarrollo :D');
});

// Al cargar la página, verifica si el modo de contraste está activo y aplícalo si es necesario.
window.addEventListener('DOMContentLoaded', () => {
  const contrastSetting = localStorage.getItem('contrastSetting');
  if (contrastSetting === 'true') {
    rootElement.classList.add('contrast');
    applyImageContrast();
  }
});

// Aplicar contraste a las imágenes
function applyImageContrast() {
  const images = document.querySelectorAll('iframe, img:not(.entidades__link-img):not(.entidades__link-img:hover):not([src="img/icons/accesibilidad-contraste.svg"])');
  images.forEach(img => {
    img.style.filter = rootElement.classList.contains('contrast') ? 'grayscale(100%)' : 'none';
  });
}

// Aumentar tamaño de fuente
toggleZoomInButton.addEventListener('click', () => {
  let fontSize = parseFloat(getComputedStyle(document.documentElement).fontSize);
  fontSize += 1;
  fontSize = Math.min(MAX_FONT_SIZE, fontSize);
  document.documentElement.style.fontSize = fontSize + 'px';
});

// Disminuir tamaño de fuente
toggleZoomOutButton.addEventListener('click', () => {
  let fontSize = parseFloat(getComputedStyle(document.documentElement).fontSize);
  fontSize -= 1;
  fontSize = Math.max(MIN_FONT_SIZE, fontSize);
  document.documentElement.style.fontSize = fontSize + 'px';
});
