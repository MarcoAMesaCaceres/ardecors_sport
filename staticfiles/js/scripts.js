document.addEventListener("DOMContentLoaded", function() {
    // Obtener la URL de la imagen del elemento script
    let imageData = document.getElementById('image-data');
    let imageUrl = imageData.dataset.imageUrl;

    // Crear un elemento de imagen
    let image = document.createElement('img');
    
    // Establecer la fuente de la imagen
    image.src = imageUrl;
    
    // Añadir una clase a la imagen para poder estilizarla
    image.classList.add('centered-image');
    
    // Añadir la imagen al body del documento
    document.body.appendChild(image);

    // Para depuración, imprime la URL en la consola
    console.log("URL de la imagen:", imageUrl);
});
