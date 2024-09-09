document.addEventListener('DOMContentLoaded', function() {
    const rows = document.querySelectorAll('tbody tr');

    rows.forEach(row => {
        row.addEventListener('click', function() {
            const productId = this.querySelector('td').textContent;
            alert(`Producto ID: ${productId}`);
            // Acciones adicionales al hacer clic en una fila
        });
    });

    const newProductButton = document.querySelector('.btn');
    if (newProductButton) {
        newProductButton.addEventListener('click', function(event) {
            event.preventDefault();
            window.location.href = this.href;
        });
    }

    console.log("Productos cargados.");
});
