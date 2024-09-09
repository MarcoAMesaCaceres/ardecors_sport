document.addEventListener('DOMContentLoaded', function() {
    const rows = document.querySelectorAll('tbody tr');

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

    console.log("Proveedores cargados.");
});