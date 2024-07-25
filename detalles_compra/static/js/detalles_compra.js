document.addEventListener('DOMContentLoaded', function() {
    // Calcula el total de la compra
    function calculateTotal() {
        let total = 0;
        const rows = document.querySelectorAll('tbody tr');
        rows.forEach(row => {
            const cantidad = parseFloat(row.querySelector('.cantidad').textContent) || 0;
            const precio = parseFloat(row.querySelector('.precio').textContent) || 0;
            total += cantidad * precio;
        });
        document.querySelector('.total-container span').textContent = total.toFixed(2);
    }

    // Llama a la función para calcular el total al cargar la página
    calculateTotal();
});