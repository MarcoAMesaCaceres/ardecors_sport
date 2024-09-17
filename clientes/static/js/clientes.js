document.addEventListener('DOMContentLoaded', function() {
    const elemento = document.getElementById('miElemento');
    if (elemento) {
        elemento.addEventListener('click', function() {
            // Acción
            const rows = document.querySelectorAll('tr'); // Asegúrate de definir 'rows'
            rows.forEach(row => {
                row.addEventListener('click', function() {
                    const providerId = this.querySelector('td').textContent;
                    alert(`Proveedor ID: ${providerId}`);
                    // Acciones adicionales al hacer clic en una fila
                });
            });

            const newProviderButton = document.querySelector('.btn');
            if (newProviderButton) {
                newProviderButton.addEventListener('click', function(event) {
                    event.preventDefault();
                    window.location.href = this.href;
                });
            }
        });
    } else {
        console.error('Elemento con id "miElemento" no encontrado.');
    }
});