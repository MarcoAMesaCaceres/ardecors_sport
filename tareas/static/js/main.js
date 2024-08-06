document.addEventListener('DOMContentLoaded', function() {
    // Toggle completed task row style
    document.querySelectorAll('.table tbody tr').forEach(function(row) {
        const completed = row.querySelector('td:nth-child(4)').innerText.trim() === 'Sí';
        if (completed) {
            row.classList.add('table-success');
        }
    });

    // Confirm task deletion
    document.querySelectorAll('.btn-danger').forEach(function(button) {
        button.addEventListener('click', function(event) {
            if (!confirm('¿Estás seguro de que deseas eliminar esta tarea?')) {
                event.preventDefault();
            }
        });
    });

    // Form validation feedback
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });
});