document.addEventListener('DOMContentLoaded', function() {
    const rows = document.querySelectorAll('tbody tr');

    rows.forEach(row => {
        row.addEventListener('click', function() {
            const userId = this.querySelector('td').textContent;
            alert(`Usuario ID: ${userId}`);
            // Acciones adicionales al hacer clic en una fila
        });
    });

    const newUserButton = document.querySelector('.btn');
    if (newUserButton) {
        newUserButton.addEventListener('click', function(event) {
            event.preventDefault();
            window.location.href = this.href;
        });
    }

    console.log("Usuarios cargados.");
});

