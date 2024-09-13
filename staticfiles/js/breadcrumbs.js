// Espera a que el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', function() {
    // Selecciona todos los enlaces dentro de los elementos del breadcrumb
    const breadcrumbLinks = document.querySelectorAll('.breadcrumb-item a');

    // Añade event listeners para cada enlace
    breadcrumbLinks.forEach(link => {
        // Cuando el mouse entra en el enlace
        link.addEventListener('mouseenter', function() {
            this.style.color = '#6f42c1'; // Cambia a violeta
            this.style.fontWeight = '800'; // Aumenta el grosor de la fuente
            this.style.textDecoration = 'underline'; // Subraya el texto
        });

        // Cuando el mouse sale del enlace
        link.addEventListener('mouseleave', function() {
            this.style.color = '#007bff'; // Vuelve a azul
            this.style.fontWeight = '700'; // Vuelve al grosor original
            this.style.textDecoration = 'none'; // Quita el subrayado
        });

        // Cuando se hace clic en el enlace
        link.addEventListener('click', function(e) {
            console.log('Navegando a:', this.textContent.trim());
            // Puedes añadir aquí más lógica si es necesario
        });
    });
});
