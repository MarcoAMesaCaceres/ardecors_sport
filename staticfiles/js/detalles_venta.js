document.addEventListener('DOMContentLoaded', function() {
    // Obtener el elemento de la tabla de detalles de venta
    const table = document.querySelector('.detalles-venta-container table');

    // Función para calcular el total
    function calculateTotal() {
        let total = 0;
        // Seleccionar todas las filas de la tabla (excepto el encabezado)
        const rows = table.querySelectorAll('tbody tr');
        
        rows.forEach(row => {
            const cantidad = parseFloat(row.querySelector('td:nth-child(2)').textContent);
            const precio = parseFloat(row.querySelector('td:nth-child(3)').textContent.replace('$', ''));
            const totalFila = cantidad * precio;
            // Agregar el total de la fila al total general
            total += totalFila;
        });

        // Mostrar el total en la página
        document.querySelector('.total-container span').textContent = `$${total.toFixed(2)}`;
    }

    // Llamar a la función para calcular el total al cargar la página
    calculateTotal();

    // Si necesitas actualizar el total al cambiar algún valor, puedes añadir eventos aquí
});
