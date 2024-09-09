    // Función para ajustar el tamaño del PDF embebido
    function resizePdfObject() {
        var pdfObject = document.querySelector('object[type="application/pdf"]');
        if (pdfObject) {
        var windowHeight = window.innerHeight;
        var containerHeight = document.querySelector('.container').offsetHeight;
        var pdfHeight = Math.min(windowHeight - 100, containerHeight - 100);
        pdfObject.style.height = pdfHeight + 'px';
        }
    }
    
    // Llamar a la función de ajuste del PDF cuando se carga la página
    window.addEventListener('load', resizePdfObject);
    
    // Llamar a la función de ajuste del PDF cuando se redimensiona la ventana
    window.addEventListener('resize', resizePdfObject);