document.addEventListener('DOMContentLoaded', function() {
    const toggleInicio = document.getElementById('toggle-inicio');
    const toggleButtons = document.getElementById('toggle-buttons');
    const toggleContrast = document.getElementById('toggle-contrast');
    const toggleZoomIn = document.getElementById('toggle-zoom-in');
    const toggleZoomOut = document.getElementById('toggle-zoom-out');
  
  
    const minFontSize = 12; // Minimum font size
    const maxFontSize = 24; // Maximum font size
  
    // Toggle accessibility buttons
    toggleInicio.addEventListener('click', function() {
        toggleButtons.classList.toggle('hidden');
        toggleButtons.classList.toggle('visible');
        toggleInicio.style.transform = toggleButtons.classList.contains('visible') ? 'translateX(0)' : 'translateX(100%)';
    });
  
    // Toggle high contrast mode
    toggleContrast.addEventListener('click', function() {
        document.body.classList.toggle('high-contrast');
    });
  
    // Increase font size
    toggleZoomIn.addEventListener('click', function() {
        fontSize = Math.min(maxFontSize, fontSize + 2);
        updateFontSize();
    });
  
    // Decrease font size
    toggleZoomOut.addEventListener('click', function() {
        fontSize = Math.max(minFontSize, fontSize - 2);
        updateFontSize();
    });
  
    function updateFontSize() {
        const paragraphs = document.getElementsByTagName('p');
        for (let p of paragraphs) {
            p.style.fontSize = `${fontSize}px`;
        }
    }
  
    // Save accessibility settings to localStorage
    function saveSettings() {
        localStorage.setItem('highContrast', document.body.classList.contains('high-contrast'));
        localStorage.setItem('fontSize', fontSize);
    }
  
    // Load accessibility settings from localStorage
    function loadSettings() {
        const highContrast = localStorage.getItem('highContrast') === 'true';
        const savedFontSize = localStorage.getItem('fontSize');
  
        if (highContrast) {
            document.body.classList.add('high-contrast');
        }
  
        if (savedFontSize) {
            fontSize = Math.max(minFontSize, Math.min(maxFontSize, parseInt(savedFontSize)));
            updateFontSize();
        }
    }
  
    // Save settings when they change
    toggleContrast.addEventListener('click', saveSettings);
    toggleZoomIn.addEventListener('click', saveSettings);
    toggleZoomOut.addEventListener('click', saveSettings);
  
    // Load settings on page load
    loadSettings();
  });