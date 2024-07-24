document.addEventListener('DOMContentLoaded', function() {
    // Obtener el formulario de configuraciones
    const form = document.querySelector('#config-form');

    // Función para mostrar un mensaje de éxito
    function showSuccessMessage(message) {
        const successMessage = document.createElement('div');
        successMessage.className = 'alert alert-success';
        successMessage.textContent = message;
        form.parentNode.insertBefore(successMessage, form);
        setTimeout(() => successMessage.remove(), 3000);
    }

    // Función para manejar el envío del formulario
    function handleFormSubmit(event) {
        event.preventDefault(); // Evita que el formulario se envíe de manera tradicional
        
        // Obtener los datos del formulario
        const formData = new FormData(form);
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value;
        });

        // Validar los datos del formulario
        if (data.nombre.trim() === '' || data.valor.trim() === '') {
            alert('Por favor, completa todos los campos.');
            return;
        }

        // Aquí puedes agregar la lógica para enviar los datos al servidor usando fetch o XMLHttpRequest
        fetch(form.action, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken') // Para enviar el token CSRF con el POST
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                showSuccessMessage('Configuración actualizada correctamente.');
            } else {
                alert('Hubo un error al actualizar la configuración.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Hubo un error al actualizar la configuración.');
        });
    }

    // Función para obtener el valor del token CSRF de las cookies
    function getCookie(name) {
        const cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    return decodeURIComponent(cookie.substring(name.length + 1));
                }
            }
        }
        return cookieValue;
    }

    // Añadir el manejador de eventos al formulario
    if (form) {
        form.addEventListener('submit', handleFormSubmit);
    }
});
