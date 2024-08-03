document.addEventListener('DOMContentLoaded', function() {
    // Obtener todas las filas de la tabla
    const rows = document.querySelectorAll('tbody tr');

    // Añadir un evento al hacer clic en cualquier fila
    rows.forEach(row => {
        row.addEventListener('click', function() {
            const orderId = this.querySelector('td').textContent;
            alert(`Orden ID: ${orderId}`);
            // Puedes redirigir o realizar acciones adicionales aquí
        });
    });

    // Función para manejar la creación de una nueva orden
    const newOrderButton = document.querySelector('.btn');
    if (newOrderButton) {
        newOrderButton.addEventListener('click', function(event) {
            event.preventDefault();
            window.location.href = this.href;
        });
    }

    console.log("Órdenes de compras cargadas.");
});
