document.addEventListener('DOMContentLoaded', function() {
    const rows = document.querySelectorAll('tbody tr');

    rows.forEach(row => {
        row.addEventListener('click', function() {
            const ventaId = this.querySelector('td').textContent;
            alert(`Venta ID: ${ventaId}`);
            // Acciones adicionales al hacer clic en una fila
        });
    });

    const newSaleButton = document.querySelector('.btn');
    if (newSaleButton) {
        newSaleButton.addEventListener('click', function(event) {
            event.preventDefault();
            window.location.href = this.href;
        });
    }

    console.log("Ventas cargadas.");
});
